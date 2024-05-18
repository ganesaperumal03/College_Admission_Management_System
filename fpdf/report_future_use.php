<?php

// Connect to database
$con2 = new mysqli("localhost", "root", "", "postform");

// Check connection
if ($con2->error) {
    die("Connection failed: " . $con2-> error);
}
$id = '2023-24 / 070';
$sqlup1 = "SELECT * FROM student_master WHERE admissionNo = '$id'";
$resultup1 = mysqli_query($con2, $sqlup1);
$row_data1 = mysqli_fetch_assoc($resultup1);

$sqlup2 = "SELECT * FROM admission_details WHERE admissionNo = '$id'";
$resultup2 = mysqli_query($con2, $sqlup2);
$row_data2 = mysqli_fetch_assoc($resultup2);

$sqlup3 = "SELECT * FROM hsc_aca WHERE admissionNo = '$id'";
$resultup3 = mysqli_query($con2, $sqlup3);
$row_data3 = mysqli_fetch_assoc($resultup3);

$sqlup4 = "SELECT * FROM additional_info WHERE admissionNo = '$id'";
$resultup4 = mysqli_query($con2, $sqlup4);
$row_data4 = mysqli_fetch_assoc($resultup4);

$sqlup5 = "SELECT * FROM fg_master WHERE admissionNo = '$id'";
$resultup5 = mysqli_query($con2, $sqlup5);
$row_data5 = mysqli_fetch_assoc($resultup5);

//-----------------------Creating Class for Watermark-----------------------------
ob_start();
require('fpdf.php');

class PDFWithWatermark extends FPDF {
    private $watermarkText;
    private $angle = 0;
    

    function SetWatermarkText($line1, $line2) {
        $this->watermarkText = array($line1, $line2);
    }

    function Footer() {
        // Add watermark
        $this->SetFont('Arial', 'B', 50);
        
        // Set watermark text color with opacity
        $this->SetTextColor(254, 195, 199);

        $x = $this->GetPageWidth() / 2;
        $y = $this->GetPageHeight() / 2;
    
        // Calculate the total height of the watermark lines
        $totalHeight = 40; // Assuming each line is 20 units high
    
        // Calculate the starting vertical position of the watermark lines
        $startY = $y - ($totalHeight / 2);
    
        // Calculate the center of the page horizontally
        $centerX = $this->GetPageWidth() / 2;
    
        // Calculate the width of each line
        $lineWidth1 = $this->GetStringWidth($this->watermarkText[0]);
        $lineWidth2 = $this->GetStringWidth($this->watermarkText[1]);
    
        // Calculate the starting horizontal position for each line
        $startX1 = $centerX - ($lineWidth1 / 2);
        $startX2 = $centerX - ($lineWidth2 / 2);

        // Set opacity for watermark
        $opacity = 0.5; // Opacity level between 0 and 1

        // Output the first line diagonally with opacity
        $this->SetTextColor(232, 237, 237);
        $this->Rotate(45, $startX1 + ($lineWidth1 / 2), $startY - 5);
        $this->Text($startX1, $startY , $this->watermarkText[0]);
        $this->Rotate(0); // Reset rotation
    
        // Output the second line diagonally with opacity
        $this->SetTextColor(213, 219, 219);
        $this->Rotate(45, $startX2 + ($lineWidth2 / 2), $startY + 30);
        $this->Text($startX2, $startY + 40, $this->watermarkText[1]);
        $this->Rotate(0); // Reset rotation

        // Reset text color after watermark
        $this->SetTextColor(0, 0, 0); // Reset text color to black
    }
    
    function Rotate($angle, $x = -1, $y = -1) {
        if ($x == -1)
            $x = $this->x;
        if ($y == -1)
            $y = $this->y;
        if ($this->angle != 0)
            $this->_out('Q');
        $this->angle = $angle;
        if ($angle != 0) {
            $angle *= M_PI / 180;
            $c = cos($angle);
            $s = sin($angle);
            $cx = $x * $this->k;
            $cy = ($this->h - $y) * $this->k;
            $this->_out(sprintf('q %.5F %.5F %.5F %.5F %.2F %.2F cm 1 0 0 1 %.2F %.2F cm', $c, $s, -$s, $c, $cx, $cy, -$cx, -$cy));
        }
    }
}

$pdf = new PDFWithWatermark();

//-------------------------------------------------------------------------------------



//----------------------------------------------------Page 1 Beginning-------------------------------------------------------


$pdf->AddPage('P', 'A4');

//Set the college logo
$pdf->Image('rit.png', 5, 5, 15, 20);

$pdf->SetY(5);
//Set the header for the form
$pdf->SetFont('Arial', 'B', 14);
$pdf->SetTextColor(50, 50, 50);
$pdf->Cell(0, 5, "RAMCO INSTITUTE OF TECHNOLOGY", 0, 1, 'C');

$pdf->SetFont('Arial', 'B', 8);
$pdf->SetTextColor(50, 50, 50);
$pdf->Cell(0, 4, "Approved by AICTE, New Delhi & Affiliated to Anna University", 0, 1, 'C');
$pdf->Cell(0, 4, "North Venganallur Village, Rajapalayam - 626 117. Virudhunagar Dist.", 0, 1, 'C');
$pdf->Cell(0, 4, "Phone : 04563 233 400, 402; E-mail : rit@ritrjpm.ac.in; www.ritrjpm.ac.in", 0, 1, 'C');


$pdf->SetFont('Arial', 'BU', 10);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 255, 51);

//APP NO.
$pdf->SetXY(25, 10);
$pdf->Cell(25, 10, $row_data1["admissionNo"], 1, 0, 'C', true);

//Other primary details

$pdf->SetFont('Arial', 'B', 7);
$pdf->SetTextColor(0, 0, 0);

$pdf->SetXY(165,5);
$pdf->Cell(25, 5, "Application from", 1, 0, 'C', true);
$pdf->SetXY(190,5);
$pdf->SetFont('Arial', '', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(15, 5, $row_data1["admissionFor"], 1, 0, 'C');

$pdf->SetFont('Arial', 'B', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(165,10);
$pdf->Cell(25, 5, "Quota", 1, 0, 'C', true);
$pdf->SetXY(190,10);
$pdf->SetFont('Arial', '', 7);
$pdf->SetTextColor(0, 0, 0);
if ($row_data1["GQ_MQ_Converted"] != '') {
    $quota = $row_data1["GQ_MQ_Converted"];
} else {
    $quota = $row_data1["quota"];
}
$pdf->Cell(15, 5, $quota, 1, 0, 'C');

$pdf->SetFont('Arial', 'B', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(165,15);
$pdf->Cell(25, 5, "Branch Alloted", 1, 0, 'C', true);
$pdf->SetXY(190,15);
$pdf->SetFont('Arial', '', 7);
$pdf->SetTextColor(0, 0, 0);
if ($row_data1["Dept_Changed"] != '') {
    $branchAll = $row_data1["Dept_Changed"];
}
else{
    $branchAll = $row_data1["branchAll"];
}
$pdf->Cell(15, 5, $branchAll, 1, 0, 'C');

$pdf->SetFont('Arial', 'B', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(165,20);
$pdf->Cell(25, 5, "Mode", 1, 0, 'C', true);
$pdf->SetXY(190,20);
$pdf->SetFont('Arial', '', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(15, 5, $row_data1["mode"], 1, 0, 'C');

$pdf->SetY(26);
$pdf->SetFont('Helvetica', 'BU', 10);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Admission Portfolio", 0, 0, 'C');

//--------------------Personal Details -----------------------------

$pdf->SetFillColor(255, 173, 51);

//Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 30);
$pdf->Cell(35, 5, "Name of the Student", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(40, 30);
$pdf->Cell(45, 5, $row_data1["name"], 1, 0, 'C');

//Gender
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(85, 30);
$pdf->Cell(10, 5, "Sex", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(95, 30);
$pdf->Cell(15, 5, $row_data1["gender"], 1, 0, 'C');

//DOB
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(110, 30);
$pdf->Cell(10, 5, "D.o.B", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(120, 30);
$pdf->Cell(20, 5, $row_data1["dob"], 1, 0, 'C');

//Age
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 35);
$pdf->Cell(10, 5, "Age", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(15, 35);
$pdf->Cell(10, 5, $row_data1["age"], 1, 0, 'C');

//Nationality
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 35);
$pdf->Cell(20, 5, "Nationality", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(45, 35);
$pdf->Cell(15, 5, $row_data1["nationality"], 1, 0, 'C');

//Religiion
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(60, 35);
$pdf->Cell(15, 5, "Religion", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(75, 35);
$pdf->Cell(20, 5, $row_data1["religion"], 1, 0, 'C');

//Mother Tounge
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(95, 35);
$pdf->Cell(25, 5, "Mother Tounge", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(120, 35);
$pdf->Cell(20, 5, $row_data1["motherto"], 1, 0, 'C');

//Nativity
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 40);
$pdf->Cell(15, 5, "Nativity", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(20, 40);
$pdf->Cell(25, 5, $row_data1["nativity"], 1, 0, 'C');

//Self Mobile Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(45, 40);
$pdf->Cell(20, 5, "Mobile No.", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(65, 40);
$pdf->Cell(20, 5, $row_data1["selfno"], 1, 0, 'C');

//Self Email ID
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(85, 40);
$pdf->Cell(15, 5, "Self Email ID", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(100, 40);
$pdf->Cell(40, 5, $row_data1["selfe"], 1, 0, 'C');

//Father Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 45);
$pdf->Cell(20, 5, "Father Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 45);
$pdf->Cell(45, 5, $row_data1["dadn"], 1, 0, 'C');

//Father Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 45);
$pdf->Cell(20, 5, "Father Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(90, 45);
$pdf->Cell(20, 5, $row_data1["dadno"], 1, 0, 'C');

//Community
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(110, 45);
$pdf->Cell(15, 5, "Community", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(125, 45);
$pdf->Cell(15, 5, $row_data1["community"], 1, 0, 'C');


//Mother Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 50);
$pdf->Cell(20, 5, "Mother Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 50);
$pdf->Cell(45, 5, $row_data1["momn"], 1, 0, 'C');

//Mother Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 50);
$pdf->Cell(20, 5, "Mother Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(90, 50);
$pdf->Cell(20, 5, $row_data1["momno"], 1, 0, 'C');

//Caste
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(110, 50);
$pdf->Cell(15, 5, "Caste", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(125, 50);
$pdf->Cell(15, 5, $row_data1["caste"], 1, 0, 'C');

//Student, Father, Mother Photos
$pdf->Image('rit.png', 147, 30.5, 19, 24);
$pdf->Image('rit.png', 166.5, 30.5, 19, 24);
$pdf->Image('rit.png', 186, 30.5, 19, 24);


//Guardian Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 55);
$pdf->Cell(20, 5, "Guardian Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 55);
$pdf->Cell(45, 5, $row_data1["guardn"], 1, 0, 'C');

//Guardian Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 55);
$pdf->Cell(20, 5, "Guardian Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(90, 55);
$pdf->Cell(15, 5, $row_data1["guardno"], 1, 0, 'C');

//Aadhaar Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(105, 55);
$pdf->Cell(20, 5, "Aadhaar Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(125, 55);
$pdf->Cell(20, 5, $row_data1["aadhaarno"], 1, 0, 'C');

//Community Certificate Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(145, 55);
$pdf->Cell(35, 5, "Community Certificate Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(180, 55);
$pdf->Cell(25, 5, $row_data1["communityno"], 1, 0, 'C');


//Displaying Permanent address
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 60);
$pdf->Cell(35, 5, "Permanent Address", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(40, 60);
$permanent_address = $row_data1["door"] . ", " . $row_data1["street"] . ", " . $row_data1["location"] . 
", " . $row_data1["taluk"] . " Taluk, " . $row_data1["district"] . " District, " . $row_data1["state"] . " - " . $row_data1["pincode"];
$pdf->Cell(165, 5, $permanent_address, 1, 0, 'C');


//Displaying Communication address
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 65);
$pdf->Cell(35, 5, "Communication Address", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(40, 65);
$communication_address = $row_data1["door1"] . ", " . $row_data1["street1"] . ", " . $row_data1["location1"] . 
", " . $row_data1["taluk1"] . " Taluk, " . $row_data1["district1"] . " District, " . $row_data1["state1"] . " - " . $row_data1["pincode1"];
$pdf->Cell(165, 5, $communication_address, 1, 0, 'C');

//----------------------------------------------------------------------------------------------------------------------------------

//Admission Details
$pdf->SetXY(5, 73);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Admission Details :", 0, 0);

//Counselling Application Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 76);
$pdf->Cell(20, 5, "Couns. App. No.", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 76);
if ((isset($row_data1["quota"]) && $row_data1["quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = $row_data2["counselNo"];
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(10, 5, $valueToStore, 1, 0, 'C');

//Counselling General Rank
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(35, 76);
$pdf->Cell(25, 5, "Couns. General Rank", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(60, 76);
if ((isset($row_data1["quota"]) && $row_data1["quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ'))  {
    $valueToStore = $row_data2["counselRank"];
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(10, 5, $valueToStore, 1, 0, 'C');

//Counselling Community Rank
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 76);
$pdf->Cell(30, 5, "Couns. Community Rank", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(100, 76);
if ((isset($row_data1["quota"]) && $row_data1["quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = "";
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(15, 5, $valueToStore, 1, 0, 'C');

//GQ Seat Allotment Order
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(115, 76);
$pdf->Cell(27, 5, "GQ Seat Allotment Order", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(142, 76);
if ((isset($row_data1["quota"]) && $row_data1["quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = $row_data2["GQseat"];
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(22, 5, $valueToStore, 1, 0, 'C');

//Management Application Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(164, 76);
$pdf->Cell(26, 5, "Management. App. No.", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(190, 76);
if ((isset($row_data1["quota"]) && $row_data1["quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = "N/A";
} else {
    $valueToStore = "";
}
$pdf->Cell(15, 5, $valueToStore, 1, 0, 'C');

//---------------------------------------------------------------------------------------------------------------

//--------------------------------------Academic Information-----------------------------
//Academic Information
$pdf->SetXY(5, 85);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Academic Information :", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);

$pdf->SetXY(5, 89);
$pdf->Cell(10, 5, "Std", 1, 0, 'C', true);
$pdf->Cell(115, 5, "Name of the School", 1, 0, 'C', true);
$pdf->Cell(10, 5, "Year", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Place", 1, 0, 'C', true);
$pdf->Cell(20, 5, "Type", 1, 0, 'C', true);
$pdf->Cell(15, 5, "Medium", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);


//EMIS
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(60, 86);
$pdf->Cell(0, 0, "a.) Emis Number : ", 0, 0);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(80);
$pdf->Cell(0, 0, $row_data2["emis"], 0, 0);


//10th School
$pdf->SetXY(5, 94);
$pdf->Cell(10, 5, "10th", 1, 0, 'C');
$pdf->Cell(115, 5, $row_data2["schoolName10"], 1, 0, 'C');
$pdf->Cell(10, 5, $row_data2["yearOfPassing10"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["place10"], 1, 0, 'C');
$pdf->Cell(20, 5, $row_data2["schooltype10"], 1, 0, 'C');
$pdf->Cell(15, 5, $row_data2["mosin10"], 1, 0, 'C');

//11th School
$pdf->SetXY(5, 99);
$pdf->Cell(10, 5, "11th", 1, 0, 'C');
$pdf->Cell(115, 5, $row_data2["schoolName11"], 1, 0, 'C');
$pdf->Cell(10, 5, $row_data2["yearOfPassing11"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["place11"], 1, 0, 'C');
$pdf->Cell(20, 5, $row_data2["schooltype11"], 1, 0, 'C');
$pdf->Cell(15, 5, $row_data2["mosin11"], 1, 0, 'C');

//12th School
$pdf->SetXY(5, 104);
$pdf->Cell(10, 5, "12th", 1, 0, 'C');
$pdf->Cell(115, 5, $row_data2["schoolName12"], 1, 0, 'C');
$pdf->Cell(10, 5, $row_data2["yearOfPassing12"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["place12"], 1, 0, 'C');
$pdf->Cell(20, 5, $row_data2["schooltype12"], 1, 0, 'C');
$pdf->Cell(15, 5, $row_data2["mosin12"], 1, 0, 'C');


//-------------------------------------------------------------


//---------------------HSC and SSLC Details-----------------------

$pdf->SetXY(5, 114);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "HSC and SSLC Details :", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);

$pdf->SetXY(38, 118);
$pdf->Cell(15, 5, "SSLC/HSC", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Register Number", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Marksheet Number", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Studied In", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Exam Number", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

//HSC
$pdf->SetXY(38, 123);
$pdf->Cell(15, 5, "HSC", 1, 0, 'C');
$pdf->Cell(30, 5, $row_data3["hscregno"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data3["hscmarkno"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data3["hscin"], 1, 0, 'C');
$pdf->Cell(30, 5, "-", 1, 0, 'C');

//SSLC
$pdf->SetXY(38, 128);
$pdf->Cell(15, 5, "SSLC", 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcregno"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcmarkno"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcin"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcexamno"], 1, 0, 'C');


//Marks Scored in HSC

$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(30,140);
$pdf->Cell(70, 5, "Marks Scored in HSC", 1, 0, 'C', true);
$pdf->SetXY(30,145);
$pdf->Cell(35, 5, "Subject", 1, 0, 'C', true);
$pdf->Cell(35, 5, "Marks Scored (Out of 100)", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

//Language
$pdf->SetXY(30,150);
$pdf->Cell(35, 5, "Language", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data3["acasub1"], 1, 0, 'C');

//English
$pdf->SetXY(30,155);
$pdf->Cell(35, 5, "English", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data3["acasub2"], 1, 0, 'C');

//Mathematics
$pdf->SetXY(30,160);
$pdf->Cell(35, 5, "Mathematics", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data3["acasub3"], 1, 0, 'C');

//Physics
$pdf->SetXY(30,165);
$pdf->Cell(35, 5, "Physics", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data3["acasub4"], 1, 0, 'C');

//Chemistry
$pdf->SetXY(30,170);
$pdf->Cell(35, 5, "Chemistry", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data3["acasub5"], 1, 0, 'C');

//Elective Marks
$pdf->SetXY(30,175);
$pdf->Cell(35, 5, $row_data3["acasub6n"], 1, 0, 'C');
$pdf->Cell(35, 5, $row_data3["acasub6"], 1, 0, 'C');


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 255, 51);
//Total
$pdf->SetXY(30,180);
$pdf->Cell(25, 5, "Total : " . $row_data3["acatot"] . " out of 600", 1, 0, 'C', true);

//Cut Off
$pdf->Cell(15, 5, "Cut Off : " . $row_data3["acacutoff"], 1, 0, 'C', true);

//PCM Average
$pdf->Cell(30, 5, "PCM Average : " . $row_data3["acapcm"] . " %", 1, 0, 'C', true);


//-------------------------------------------------------------------------------------


//Marks Scored in SSLC

$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 173, 51);

$pdf->SetXY(120,140);
$pdf->Cell(60, 5, "Marks Scored in SSLC", 1, 0, 'C', true);
$pdf->SetXY(120,145);
$pdf->Cell(30, 5, "Subject", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Marks Scored", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

//Language
$pdf->SetXY(120,150);
$pdf->Cell(30, 5, $row_data2["sslcsub1"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcsubm1"] . " out of " . $row_data2["sslcout1"], 1, 0, 'C');

//English
$pdf->SetXY(120,155);
$pdf->Cell(30, 5, $row_data2["sslcsub2"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcsubm2"] . " out of " . $row_data2["sslcout2"], 1, 0, 'C');

//Mathematics
$pdf->SetXY(120,160);
$pdf->Cell(30, 5, $row_data2["sslcsub3"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcsubm3"] . " out of " . $row_data2["sslcout3"], 1, 0, 'C');

//Science
$pdf->SetXY(120,165);
$pdf->Cell(30, 5, $row_data2["sslcsub4"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcsubm4"] . " out of " . $row_data2["sslcout4"], 1, 0, 'C');

//Social Science
$pdf->SetXY(120,170);
$pdf->Cell(30, 5, $row_data2["sslcsub5"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["sslcsubm5"] . " out of " . $row_data2["sslcout5"], 1, 0, 'C');

//Elective Subject
$pdf->SetXY(120,175);

if (!isset($row_data2["sslcsub6"]) || $row_data2["sslcsub6"] === '') {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data2["sslcsub6"];
}

$pdf->Cell(30, 5, $valueToStore, 1, 0, 'C');

//Elective Marks
if (!isset($row_data2["sslcsubm6"]) || $row_data2["sslcsubm6"] === '0') {
    $elecmarks = "0";
} else {
    $elecmarks = $row_data2["sslcsubm6"];
}

//Elective Maximum
if (!isset($row_data2["sslcout6"]) || $row_data2["sslcout6"] === '0') {
    $elecmax = "100";
} else {
    $elecmax = $row_data2["sslcout6"];
}

$pdf->Cell(30, 5, $elecmarks . " out of " . $elecmax, 1, 0, 'C');


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 255, 51);
//Total
$pdf->SetXY(120,180);
$pdf->Cell(60, 5, "Total : " . $row_data2["sscltot"] . " out of " . $row_data2["sslcout"], 1, 0, 'C', true);


//-----------------------------------------------------------------------------------------

//----------------------------------------------Watermark-------------------------------
// Set custom font
$pdf->SetFont('Arial', 'B', 18);

// Extracting $dep from $row_data1["branchAll"]
$branchAll = $row_data1["branchAll"];
$words = explode(' ', $branchAll);
$dep = end($words);

// Set watermark text
$admissionFor = $row_data1["admissionFor"];
if ($admissionFor == "I Year") {
    $watermarkText = "FY" . "/" . $row_data1["quota"] . "/" . $dep . "/2023-24";
} elseif ($admissionFor == "LE") {
    $watermarkText = "LE" . "/" . $row_data1["quota"] . "/" . $dep . "/2023-24";
} else {
    $watermarkText = ""; // Set default watermark text or handle other cases
}

$pdf->SetWatermarkText("", $watermarkText);

//--------------------------------------------------------------------------------------------

$pdf->SetY(276);
$pdf->SetFont('Arial', '', 8);
date_default_timezone_set('Asia/Kolkata');
$date = date('F j, Y, g:i, a');
$pdf->Cell(0,0,'Generated On ' . $date,0 ,1, 'R');


//-------------------------------------------------End of Page 1----------------------------------------------------

//-------------------------------------------Page 2 Beginning-------------------------------------------------------

$pdf->AddPage('P', 'A4');


//---------------------------Special Reservation--------------------------------------

$pdf->SetXY(5, 30);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Special Reservation :", 0, 0);

$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(15, 38);
$pdf->Cell(0, 0, "Category :", 0, 0);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(27, 38);
$pdf->Cell(0, 0, "Fill the DB Value here", 0, 0);

//--------------------------------------------------------------------------------------

//---------------------------Parent Occupation-----------------------------------

$pdf->SetXY(5, 48);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Occupation of Parent / Guardian :", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 173, 51);
$pdf->SetXY(65, 56);
$pdf->Cell(30, 5, "Occupation", 1, 0, 'C', true);
$pdf->Cell(50, 5, "Job Details", 1, 0, 'C', true);

$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(65, 61);
$pdf->Cell(30, 5, $row_data4["occupation"], 1, 0, 'C');
$pdf->Cell(50, 5, $row_data4["job"], 1, 0, 'C');


$pdf->SetXY(65,71);
$pdf->Cell(0, 0, "Family Annual Income of Parent / Guardian   : ", 0, 0, 'L');
$pdf->SetXY(110,71);
$pdf->Cell(0, 0, $row_data4["income"], 0, 0, 'L');
$pdf->SetXY(65,75);
$pdf->Cell(0, 0, "(As per Income Certificate)", 0, 0, 'L');

//--------------------------------------------------------------------------------

//---------------------------Scholarship Information------------------------------

$pdf->SetXY(5, 82);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Scholarship Information : (Only GQ)", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 88);
$pdf->Cell(20, 5, "Std.", 1, 0, 'C', true);
$pdf->Cell(115, 5, "School Name", 1, 0, 'C', true);
$pdf->Cell(30, 5, "School Type", 1, 0, 'C', true);


//6th - 10th
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 93);
$pdf->Cell(20, 5, "6th - 10th", 1, 0, 'C');
if (!isset($row_data4['smallschool']) || $row_data4['smallschool'] === '' || $row_data1["quota"] === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data4['smallschool'];
}
$pdf->Cell(115, 5, $valueToStore, 1, 0, 'C');
if (!isset($row_data4['schooltype']) || $row_data4['schooltype'] === '' || $row_data1["quota"] === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data4['schooltype'];
}
$pdf->Cell(30, 5, $valueToStore, 1, 0, 'C');


//11th - 12th
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 98);
$pdf->Cell(20, 5, "11th - 12th", 1, 0, 'C');
if (!isset($row_data4['bigschool']) || $row_data4['bigschool'] === '' || $row_data1["quota"] === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data4['bigschool'];
}
$pdf->Cell(115, 5, $valueToStore, 1, 0, 'C');
if (!isset($row_data4['schooltype1']) || $row_data4['schooltype1'] === '' || $row_data1["quota"] === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data4['schooltype1'];
}
$pdf->Cell(30, 5, $valueToStore, 1, 0, 'C');


//---------------------------------------------------------------------------------------------------

//---------------------------------------Student Bank Account Details--------------------------------------------

//Student Account
$pdf->SetXY(5, 110);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Student Bank Account Details :", 0, 0);

//Account Holder Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 117);
$pdf->Cell(25, 5, "Account Holder Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["bankholder"], 1, 0, 'C');

//Bank Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 122);
$pdf->Cell(25, 5, "Bank Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["bankn"], 1, 0, 'C');

//Branch Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 127);
$pdf->Cell(25, 5, "Branch Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["branchn"], 1, 0, 'C');

//Branch Code
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 132);
$pdf->Cell(25, 5, "Branch Code", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["branchcode"], 1, 0, 'C');

//IFSC Code
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 137);
$pdf->Cell(25, 5, "IFSC Code", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["ifsc"], 1, 0, 'C');

//MICR Code
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 142);
$pdf->Cell(25, 5, "MICR Code", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["micr"], 1, 0, 'C');

//Account Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 147);
$pdf->Cell(25, 5, "Account Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data4["accountno"], 1, 0, 'C');

//----------------------------End of Student Bank Details--------------------------------


//---------------------------Joint Declaration---------------------------------

$pdf->SetY(160);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "JOINT DECLARATION BY THE APPLICANT AND PARENT / GUARDIAN", 0, 0, 'C');


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

$text = "We hereby solemnly affirm that the information furnished by us in the Application form and also in the enclosure there to submitted by us are true. If any information furnished therein is untrue in material particulars or on verification at a later stage, we are liable for criminal prosecution and we also agree to forgo the seat in this Institution / for removal of student's name from roll of the Institution at whatever the stage of study he/she may be at the time of detection of such wrong particulars. If admitted, we agree to abide by the rules and regulations of the Institution and submit the Anti-ragging Affidavits by the Student and by the Parent within 2 weeks from the date of  commencement of the Semester / College reopening. In the event of any violation of the College rules / Hostel rules by the Student we agree to obey the action taken by the Institution.";

// Add the text to the PDF
$pdf->SetXY(10, 165);
$pdf->MultiCell(0, 5, $text, 0, 'L');


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);

//Parent Signature
$pdf->SetXY(35, 196);
$pdf->Cell(0, 0, "Signature of the Parent / Guardian", 0, 0);
$pdf->SetXY(35, 208);
$pdf->Cell(0, 0, "Name : " . $row_data1["dadn"], 0, 0);

//Student Signature
$pdf->SetXY(140, 196);
$pdf->Cell(0, 0, "Signature of the Student", 0, 0);
$pdf->SetXY(140, 208);
$pdf->Cell(0, 0, "Name : " . $row_data1["name"], 0, 0);

//Place
$pdf->SetXY(35, 215);
$pdf->Cell(0, 0, "Place : Rajapalayam", 0, 0);

//Date of admission
$dateOfAdmission = date('d-m-Y', strtotime($row_data4["dateadmission"]));
$pdf->SetXY(140, 215);
$pdf->Cell(0, 0, "Date of Admission : " . $dateOfAdmission, 0, 0);

//------------------------------------End of Joint Declaration Details-----------------------------------------


//------------------------------------Office Use Details--------------------------------------

$pdf->SetY(225);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "FOR OFFICE USE", 0, 0, 'C');

//Admission Status
$pdf->SetXY(60,235);
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(35, 5, "ADMISSION STATUS", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(60, 5, "Admitted", 1, 0, 'C');

//Quota
$pdf->SetXY(60,240);
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(35, 5, "ADMITTED UNDER QUOTA", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(60, 5, $quota, 1, 0, 'C');

//Branch Allotted
$pdf->SetXY(60,245);
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(35, 5, "BRANCH ALLOTTED", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
if ($branchAll == "B.TECH AD") {
    $branchAll = "B.Tech Artificial Intelligence and Data Science";
} elseif ($branchAll == "B.E CSE") {
    $branchAll = "B.E.Computer Science and Engineering";
} elseif ($branchAll == "B.TECH CSBS") {
    $branchAll = "B.Tech Computer Science and Business System";
} elseif ($branchAll == "B.E EEE") {
    $branchAll = "B.E.Electrical and Electronics Engineering";
} elseif ($branchAll == "B.E ECE") {
    $branchAll = "B.E.Electronics and Communication Engineering";
} elseif ($branchAll == "B.E CIVIL") {
    $branchAll = "B.E.Civil Engineering";
} elseif ($branchAll == "B.E MECH") {
    $branchAll = "B.E.Mechanical Engineering";
} elseif ($branchAll == "B.TECH IT") {
    $branchAll = "B.Tech.Information Technology";
}
$pdf->Cell(60, 5, $branchAll, 1, 0, 'C');


//GM(ADMIN) Signature
$pdf->SetXY(40,265);
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "GM(ADMIN)", 0, 0);

//Principal Signature
$pdf->SetXY(170,265);
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Principal", 0, 0);




$pdf->SetY(276);
$pdf->SetFont('Arial', '', 6);
date_default_timezone_set('Asia/Kolkata');
$date = date('F j, Y, g:i, a');
$pdf->Cell(0,0,'Generated On ' . $date,0 ,1, 'R');

$pdf->Output();
ob_end_flush(); 


?>