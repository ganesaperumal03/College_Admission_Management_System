<?php

// Connect to database
$con2 = new mysqli("localhost", "root", "", "admissionform");

// Check connection
if ($con2->error) {
    die("Connection failed: " . $con2-> error);
}
$id = $_GET['admissionNo'];
$sqlup1 = "SELECT * FROM application_personal_details WHERE admissionNo = '$id'";
$resultup1 = mysqli_query($con2, $sqlup1);
$row_data1 = mysqli_fetch_assoc($resultup1);

$sqlup2 = "SELECT * FROM application_hsc_marks WHERE admissionNo = '$id'";
$resultup2 = mysqli_query($con2, $sqlup2);
$row_data2 = mysqli_fetch_assoc($resultup2);

$sqlup3 = "SELECT * FROM application_academic_details WHERE admissionNo = '$id'";
$resultup3 = mysqli_query($con2, $sqlup3);
$row_data3 = mysqli_fetch_assoc($resultup3);

//-----------------------Creating Class for Watermark-----------------------------
ob_start();
require('fpdf.php');


$pdf = new FPDF();

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
    $quota = $row_data1["Quota"];
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
    $branchAll = $row_data1["Department"];
}
$pdf->Cell(15, 5, $branchAll, 1, 0, 'C');

$pdf->SetFont('Arial', 'B', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(165,20);
$pdf->Cell(25, 5, "Mode", 1, 0, 'C', true);
$pdf->SetXY(190,20);
$pdf->SetFont('Arial', '', 7);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(15, 5, $row_data1["Mode"], 1, 0, 'C');

$pdf->SetY(26);
$pdf->SetFont('Helvetica', 'BU', 10);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Admission Portfolio", 0, 0, 'C');

//--------------------Personal Details -----------------------------

//Address Details
$pdf->SetXY(5, 36);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Personal Details :", 0, 0);


$pdf->SetFillColor(255, 173, 51);

//Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 43);
$pdf->Cell(35, 5, "Name of the Student", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(40);
$pdf->Cell(45, 5, $row_data1["Name"], 1, 0, 'C');

//Gender
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(85);
$pdf->Cell(10, 5, "Sex", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
$pdf->Cell(15, 5, $row_data1["Gender"], 1, 0, 'C');

//DOB
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(110);
$pdf->Cell(10, 5, "D.o.B", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(120);
$pdf->Cell(20, 5, $row_data1["Date_of_Birth"], 1, 0, 'C');

//Age
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 48);
$pdf->Cell(10, 5, "Age", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(15);
$pdf->Cell(10, 5, $row_data1["Age"], 1, 0, 'C');

//Nationality
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(25);
$pdf->Cell(20, 5, "Nationality", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(45);
$pdf->Cell(15, 5, $row_data1["Nationality"], 1, 0, 'C');

//Religiion
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(60);
$pdf->Cell(15, 5, "Religion", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(75);
$pdf->Cell(20, 5, $row_data1["Religion"], 1, 0, 'C');

//Mother Tounge
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
$pdf->Cell(25, 5, "Mother Tounge", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(120);
$pdf->Cell(20, 5, $row_data1["Mother_Tongue"], 1, 0, 'C');

//Nativity
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 53);
$pdf->Cell(15, 5, "Nativity", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(20);
$pdf->Cell(25, 5, $row_data1["Nativity"], 1, 0, 'C');

//Self Mobile Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(45);
$pdf->Cell(20, 5, "Mobile No.", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(65);
$pdf->Cell(20, 5, $row_data1["Self_Mobile_Number"], 1, 0, 'C');

//Self Email ID
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(85);
$pdf->Cell(15, 5, "Self Email ID", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(100);
$pdf->Cell(40, 5, $row_data1["Self_Email_ID"], 1, 0, 'C');

//Father Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 58);
$pdf->Cell(20, 5, "Father Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(25);
$pdf->Cell(45, 5, $row_data1["Father_name"], 1, 0, 'C');

//Father Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(70);
$pdf->Cell(20, 5, "Father Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(90);
$pdf->Cell(20, 5, $row_data1["Father_Mobile_Number"], 1, 0, 'C');

//Community
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(110);
$pdf->Cell(15, 5, "Community", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(125);
$pdf->Cell(15, 5, $row_data1["Community"], 1, 0, 'C');


//Mother Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 63);
$pdf->Cell(20, 5, "Mother Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(25);
$pdf->Cell(45, 5, $row_data1["Mother_name"], 1, 0, 'C');

//Mother Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(70);
$pdf->Cell(20, 5, "Mother Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(90);
$pdf->Cell(20, 5, $row_data1["Mother_Mobile_Number"], 1, 0, 'C');

//Caste
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(110);
$pdf->Cell(15, 5, "Caste", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(125);
$pdf->Cell(15, 5, $row_data1["Caste"], 1, 0, 'C');

$Profile_Image = $row_data1["Profile_Image"];
$Father_Profile_Image = $row_data1["Father_Profile_Image"];
$Mother_Profile_Image = $row_data1["Mother_Profile_Image"];

// Construct the file paths based on the admission number
$studentPhotoPath = "C:/Users/rit/Downloads/New admissio portal/" . $Profile_Image;
$fatherPhotoPath = "C:/Users/rit/Downloads/New admissio portal/" . $Father_Profile_Image;
$motherPhotoPath = "C:/Users/rit/Downloads/New admissio portal/" . $Mother_Profile_Image;

$pdf->Image($studentPhotoPath, 147, 43.5, 19, 24);
$pdf->Image($fatherPhotoPath, 166.5, 43.5, 19, 24);
$pdf->Image($motherPhotoPath, 186, 43.5, 19, 24);


//Guardian Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 68);
$pdf->Cell(20, 5, "Guardian Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(25);
$pdf->Cell(45, 5, $row_data1["Guardian_name"], 1, 0, 'C');

//Guardian Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(70);
$pdf->Cell(20, 5, "Guardian Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(90);
$pdf->Cell(15, 5, $row_data1["Guardian_Father_Mobile_No"], 1, 0, 'C');

//Aadhaar Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(105);
$pdf->Cell(20, 5, "Aadhaar Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(125);
$pdf->Cell(20, 5, $row_data1["Aadhaar_Number"], 1, 0, 'C');

//Community Certificate Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(145);
$pdf->Cell(35, 5, "Community Certificate Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(180);
$pdf->Cell(25, 5, $row_data1["CommunityNumber"], 1, 0, 'C');

//---------------------------------------------------------------------------------------

//----------------------------------Address Details--------------------------------------

//Address Details
$pdf->SetXY(5, 80);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Address Details :", 0, 0);

//Displaying Permanent address
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 86);
$pdf->Cell(35, 5, "Permanent Address", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(40);
$permanent_address = $row_data1["Permanent_Address_Door_No"] . ", " . $row_data1["Permanent_Address_Street_Name"] . ", " . $row_data1["Permanent_Address_Location"] . 
", " . $row_data1["Permanent_Address_Taluk"] . " Taluk, " . $row_data1["Permanent_Address_District"] . " District, " . $row_data1["Permanent_Address_State"] . " - " . $row_data1["Permanent_Address_Pincode"];
$pdf->Cell(165, 5, $permanent_address, 1, 0, 'C');

//Displaying Communication address
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(5, 91);
$pdf->Cell(35, 5, "Communication Address", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(40);
$communication_address = $row_data1["Communication_Address_Door_No"] . ", " . $row_data1["Communication_Address_Street_Name"] . ", " . $row_data1["Communication_Address_Location"] . 
", " . $row_data1["Communication_Address_Taluk"] . " Taluk, " . $row_data1["Communication_Address_District"] . " District, " . $row_data1["Communication_Address_State"] . " - " . $row_data1["Communication_Address_Pincode"];
$pdf->Cell(165, 5, $communication_address, 1, 0, 'C');

//----------------------------------------------------------------------------------------------------------------------------------

//Admission Details
$pdf->SetXY(5, 103);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Admission Details :", 0, 0);

//Counselling Application Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(50, 110);
$pdf->Cell(45, 5, "Counselling Application Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
if ((isset($row_data1["Quota"]) && $row_data1["Quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = $row_data3["Counselling_Application_No"];
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(25, 5, $valueToStore, 1, 0, 'C');

//Counselling General Rank
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(50, 115);
$pdf->Cell(45, 5, "Counselling General Rank", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
if ((isset($row_data1["Quota"]) && $row_data1["Quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ'))  {
    $valueToStore = $row_data3["Counselling_General_Rank"];
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(25, 5, $valueToStore, 1, 0, 'C');

//Counselling Community Rank
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(50, 120);
$pdf->Cell(45, 5, "Counselling Community Rank", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
if ((isset($row_data1["Quota"]) && $row_data1["Quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = "";
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(25, 5, $valueToStore, 1, 0, 'C');

//GQ Seat Allotment Order
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(50, 125);
$pdf->Cell(45, 5, "GQ Seat Allotment Order", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
if ((isset($row_data1["Quota"]) && $row_data1["Quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = $row_data3["GQ_Admission_Number"];
} else {
    $valueToStore = "N/A";
}
$pdf->Cell(25, 5, $valueToStore, 1, 0, 'C');

//Management Application Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(50, 130);
$pdf->Cell(45, 5, "Management Application Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(95);
if ((isset($row_data1["Quota"]) && $row_data1["Quota"] === 'GQ') || ($row_data1["GQ_MQ_Converted"] === 'GQ')) {
    $valueToStore = "N/A";
} else {
    $valueToStore = "";
}
$pdf->Cell(25, 5, $valueToStore, 1, 0, 'C');

//---------------------------------------------------------------------------------------------------------------

//--------------------------------------Academic Information-----------------------------
//Academic Information
$pdf->SetXY(5, 142);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Academic Information :", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);

$pdf->SetXY(5, 150);
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
$pdf->SetXY(60, 145);
$pdf->Cell(0, 0, "a.) Emis Number : ", 0, 0);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetX(80);
$pdf->Cell(0, 0, $row_data1["EMIS_ID"], 0, 0);


//10th School
$pdf->SetXY(5, 155);
$pdf->Cell(10, 5, "10th", 1, 0, 'C');
$pdf->Cell(115, 5, $row_data1["Tenth_Std_School_Name"], 1, 0, 'C');
$pdf->Cell(10, 5, $row_data1["Tenth_Std_Year_of_Passing"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Place_of_School"], 1, 0, 'C');
$pdf->Cell(20, 5, $row_data1["Tenth_Std_School_Type"], 1, 0, 'C');
$pdf->Cell(15, 5, $row_data1["Tenth_Std_Medium_of_Study"], 1, 0, 'C');

//11th School
$pdf->SetXY(5, 160);
$pdf->Cell(10, 5, "11th", 1, 0, 'C');
$pdf->Cell(115, 5, $row_data2["Eleventh_Std_School_Name"], 1, 0, 'C');
$pdf->Cell(10, 5, $row_data2["Eleventh_Std_Year_of_Passing"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["Eleventh_Std_Place_of_School"], 1, 0, 'C');
$pdf->Cell(20, 5, $row_data2["Eleventh_Std_Category"], 1, 0, 'C');
$pdf->Cell(15, 5, $row_data2["Eleventh_Std_Medium_of_Study"], 1, 0, 'C');

//12th School
$pdf->SetXY(5, 165);
$pdf->Cell(10, 5, "12th", 1, 0, 'C');
$pdf->Cell(115, 5, $row_data2["Twelfth_Std_School_Name"], 1, 0, 'C');
$pdf->Cell(10, 5, $row_data2["Twelfth_Std_Year_of_Passing"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["Twelfth_Std_Place_of_School"], 1, 0, 'C');
$pdf->Cell(20, 5, $row_data2["Twelfth_Std_Category"] . "&" . $row_data2["Twelfth_Std_Education_Qualified"], 1, 0, 'C');
$pdf->Cell(15, 5, $row_data2["Twelfth_Std_Medium_of_Study"], 1, 0, 'C');


//-------------------------------------------------------------


//---------------------HSC and SSLC Details-----------------------

$pdf->SetXY(5, 180);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "HSC and SSLC Details :", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);

$pdf->SetXY(38, 190);
$pdf->Cell(15, 5, "SSLC/HSC", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Register Number", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Marksheet Number", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Studied In", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Exam Number", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

//HSC
$pdf->SetXY(38, 195);
$pdf->Cell(15, 5, "HSC", 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["Twelfth_Std_Register_No"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["Twelfth_Std_Marksheet_No"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data2["Twelfth_Std_studied_in"], 1, 0, 'C');
$pdf->Cell(30, 5, "-", 1, 0, 'C');

//SSLC
$pdf->SetXY(38, 200);
$pdf->Cell(15, 5, "SSLC", 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Register_No"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Marksheet_No"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Studied_In"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Roll_No"], 1, 0, 'C');


//Marks Scored in HSC

$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(30,220);
$pdf->Cell(70, 5, "Marks Scored in HSC", 1, 0, 'C', true);
$pdf->SetXY(30,225);
$pdf->Cell(35, 5, "Subject", 1, 0, 'C', true);
$pdf->Cell(35, 5, "Marks Scored (Out of 100)", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

//Language
$pdf->SetXY(30,230);
$pdf->Cell(35, 5, "Language", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_Language_Mark"], 1, 0, 'C');

//English
$pdf->SetXY(30,235);
$pdf->Cell(35, 5, "English", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_English_Mark"], 1, 0, 'C');

//Mathematics
$pdf->SetXY(30,240);
$pdf->Cell(35, 5, "Chemistry", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_chemistry_Mark"], 1, 0, 'C');

//Physics
$pdf->SetXY(30,245);
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_Mathematics_or_Physics_Name"], 1, 0, 'C');
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_Mathematics_or_Physics_Mark"], 1, 0, 'C');

//Chemistry
$pdf->SetXY(30,250);
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_Vocational_Theory_Name"], 1, 0, 'C');
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_Vocational_Theory_Mark"], 1, 0, 'C');

//Elective Marks
$pdf->SetXY(30,255);
$pdf->Cell(35, 5, "Practical", 1, 0, 'C');
$pdf->Cell(35, 5, $row_data2["Twelfth_Std_voc_Practical_Mark"], 1, 0, 'C');


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 255, 51);
//Total
$pdf->SetXY(30,260);
$pdf->Cell(26, 5, "Total : " . $row_data2["Twelfth_Std_voc_Total_Marks"] . " out of 600", 1, 0, 'C', true);

//Cut Off
$pdf->Cell(18, 5, "Cut Off : " . $row_data2["Twelfth_Std_voc_CUT_OFF_Mark"], 1, 0, 'C', true);

//PCM Average
$pdf->Cell(26, 5, "PCM Average : " . $row_data2["Twelfth_Std_voc_PCM_Average"] . " %", 1, 0, 'C', true);


//-------------------------------------------------------------------------------------


//Marks Scored in SSLC

$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 173, 51);

$pdf->SetXY(120,220);
$pdf->Cell(60, 5, "Marks Scored in SSLC", 1, 0, 'C', true);
$pdf->SetXY(120,225);
$pdf->Cell(30, 5, "Subject", 1, 0, 'C', true);
$pdf->Cell(30, 5, "Marks Scored", 1, 0, 'C', true);


$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);

//Language
$pdf->SetXY(120,230);
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Tamil_Name"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Tamil_Mark"] . " out of " . $row_data1["Tenth_Std_Tamil_Obtain_Mark"], 1, 0, 'C');

//English
$pdf->SetXY(120,235);
$pdf->Cell(30, 5, $row_data1["Tenth_Std_English_Name"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_English_Mark"] . " out of " . $row_data1["Tenth_Std_English_Obtain_Mark"], 1, 0, 'C');

//Mathematics
$pdf->SetXY(120,240);
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Maths_Name"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Maths_Mark"] . " out of " . $row_data1["Tenth_Std_Maths_Obtain_Mark"], 1, 0, 'C');

//Science
$pdf->SetXY(120,245);
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Science_Name"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_Science_Mark"] . " out of " . $row_data1["Tenth_Std_Science_Obtain_Mark"], 1, 0, 'C');

//Social Science
$pdf->SetXY(120,250);
$pdf->Cell(30, 5, $row_data1["Tenth_Std_SocialScience_Name"], 1, 0, 'C');
$pdf->Cell(30, 5, $row_data1["Tenth_Std_SocialScience_Mark"] . " out of " . $row_data1["Tenth_Std_SocialScience_Obtain_Mark"], 1, 0, 'C');

//Elective Subject
$pdf->SetXY(120,255);

if (!isset($row_data1["Tenth_Std_Others_Name"]) || $row_data1["Tenth_Std_Others_Name"] === '') {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data1["Tenth_Std_Others_Name"];
}

$pdf->Cell(30, 5, $valueToStore, 1, 0, 'C');

//Elective Marks
if (!isset($row_data1["Tenth_Std_Others_Mark"]) || $row_data1["Tenth_Std_Others_Mark"] === '0') {
    $elecmarks = "0";
} else {
    $elecmarks = $row_data1["Tenth_Std_Others_Mark"];
}

//Elective Maximum
if (!isset($row_data1["Tenth_Std_Others_Obtain_Mark"]) || $row_data1["Tenth_Std_Others_Obtain_Mark"] === '0') {
    $elecmax = "100";
} else {
    $elecmax = $row_data1["Tenth_Std_Others_Obtain_Mark"];
}

$pdf->Cell(30, 5, $elecmarks . " out of " . $elecmax, 1, 0, 'C');


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 255, 51);
//Total
$pdf->SetXY(120,260);
$pdf->Cell(60, 5, "Total : " . $row_data1["Tenth_Std_Obtain_Mark"] . " out of " . $row_data1["Tenth_Std_Total_Mark"], 1, 0, 'C', true);


//-----------------------------------------------------------------------------------------

// //----------------------------------------------Watermark-------------------------------
// // Set custom font
// $pdf->SetFont('Arial', 'B', 18);

// // Extracting $dep from $row_data1["branchAll"]
// $branchAll = $row_data1["branchAll"];
// $words = explode(' ', $branchAll);
// $dep = end($words);

// // Set watermark text
// $admissionFor = $row_data1["admissionFor"];
// if ($admissionFor == "I Year") {
//     $watermarkText = "FY" . "/" . $row_data1["quota"] . "/" . $dep . "/2023-24";
// } elseif ($admissionFor == "LE") {
//     $watermarkText = "LE" . "/" . $row_data1["quota"] . "/" . $dep . "/2023-24";
// } else {
//     $watermarkText = ""; // Set default watermark text or handle other cases
// }

// $pdf->SetWatermarkText("", $watermarkText);

// //--------------------------------------------------------------------------------------------

$pdf->SetY(276);
$pdf->SetFont('Arial', '', 8);
date_default_timezone_set('Asia/Kolkata');
$date = date('F j, Y, g:i, a');
$pdf->Cell(0,0,'Generated On ' . $date,0 ,1, 'R');


//-------------------------------------------------End of Page 1----------------------------------------------------

//-------------------------------------------Page 2 Beginning-------------------------------------------------------

$pdf->AddPage('P', 'A4');


//---------------------------Special Reservation--------------------------------------

$pdf->SetXY(5, 15);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Special Reservation :", 0, 0);

$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 173, 51);
$pdf->SetXY(55, 20);
$pdf->Cell(25, 5, "Scholarship", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(80, 20);
$pdf->Cell(70, 5, $row_data3["ScholarShip"], 1, 0, 'C');

//--------------------------------------------------------------------------------------

//---------------------------Parent Occupation-----------------------------------

$pdf->SetXY(5, 35);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Occupation of Parent / Guardian :", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetFillColor(255, 173, 51);
$pdf->SetXY(65, 42);
$pdf->Cell(30, 5, "Occupation", 1, 0, 'C', true);
$pdf->Cell(50, 5, "Job Details", 1, 0, 'C', true);

$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(65, 47);
$pdf->Cell(30, 5, $row_data3["Occupation"], 1, 0, 'C');
$pdf->Cell(50, 5, $row_data3["Job_Details"], 1, 0, 'C');


$pdf->SetXY(65,57);
$pdf->Cell(0, 0, "Family Annual Income of Parent / Guardian   : ", 0, 0, 'L');
$pdf->SetXY(110,57);
$pdf->Cell(0, 0, $row_data3["Annual_Income"], 0, 0, 'L');
$pdf->SetXY(65,61);
$pdf->Cell(0, 0, "(As per Income Certificate)", 0, 0, 'L');

//--------------------------------------------------------------------------------

//---------------------------Scholarship Information------------------------------

$pdf->SetXY(5, 72);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Scholarship Information : (Only GQ)", 0, 0);


$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 78);
$pdf->Cell(20, 5, "Std.", 1, 0, 'C', true);
$pdf->Cell(115, 5, "School Name", 1, 0, 'C', true);
$pdf->Cell(30, 5, "School Type", 1, 0, 'C', true);


//6th - 10th
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 83);
$pdf->Cell(20, 5, "6th - 10th", 1, 0, 'C');
if (!isset($row_data3['Name_of_Std_6th_10th']) || $row_data3['Name_of_Std_6th_10th'] === '' || $quota === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data3['Name_of_Std_6th_10th'];
}
$pdf->Cell(115, 5, $valueToStore, 1, 0, 'C');
if (!isset($row_data3['Std_6th_10th_schooltype']) || $row_data3['Std_6th_10th_schooltype'] === '' || $quota  === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data3['Std_6th_10th_schooltype'];
}
$pdf->Cell(30, 5, $valueToStore, 1, 0, 'C');


//11th - 12th
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(25, 88);
$pdf->Cell(20, 5, "11th - 12th", 1, 0, 'C');
if (!isset($row_data3['School_Name_of_Std_11th_12th']) || $row_data3['School_Name_of_Std_11th_12th'] === '' || $quota === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data3['School_Name_of_Std_11th_12th'];
}
$pdf->Cell(115, 5, $valueToStore, 1, 0, 'C');
if (!isset($row_data3['Std_11th_12th_School_Type']) || $row_data3['Std_11th_12th_School_Type'] === '' || $quota === "MQ") {
    $valueToStore = "N/A";
} else {
    $valueToStore = $row_data3['Std_11th_12th_School_Type'];
}
$pdf->Cell(30, 5, $valueToStore, 1, 0, 'C');


//---------------------------------------------------------------------------------------------------

//---------------------------------------Student Bank Account Details--------------------------------------------

//Student Account
$pdf->SetXY(5, 103);
$pdf->SetFont('Helvetica', 'BU', 9);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(0, 0, "Student Bank Account Details :", 0, 0);

//Account Holder Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 110);
$pdf->Cell(25, 5, "Account Holder Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["Bank_Holder_Name"], 1, 0, 'C');

//Bank Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 115);
$pdf->Cell(25, 5, "Bank Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["Name_of_the_Bank"], 1, 0, 'C');

//Branch Name
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 120);
$pdf->Cell(25, 5, "Branch Name", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["Branch_Name_of_the_Bank"], 1, 0, 'C');

//Branch Code
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 125);
$pdf->Cell(25, 5, "Branch Code", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["Branch_Code_No"], 1, 0, 'C');

//IFSC Code
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 130);
$pdf->Cell(25, 5, "IFSC Code", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["IFSC"], 1, 0, 'C');

//MICR Code
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 135);
$pdf->Cell(25, 5, "MICR Code", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["MICR"], 1, 0, 'C');

//Account Number
$pdf->SetFont('Arial', 'B', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(70, 140);
$pdf->Cell(25, 5, "Account Number", 1, 0, 'C', true);
$pdf->SetFont('Arial', '', 6);
$pdf->SetTextColor(0, 0, 0);
$pdf->Cell(50, 5, $row_data3["Account_No"], 1, 0, 'C');

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
$pdf->Cell(0, 0, "Name : " . $row_data1["Father_name"], 0, 0);

//Student Signature
$pdf->SetXY(140, 196);
$pdf->Cell(0, 0, "Signature of the Student", 0, 0);
$pdf->SetXY(140, 208);
$pdf->Cell(0, 0, "Name : " . $row_data1["Name"], 0, 0);

//Place
$pdf->SetXY(35, 215);
$pdf->Cell(0, 0, "Place : Rajapalayam", 0, 0);

//Date of admission
$dateOfAdmission = date('d-m-Y', strtotime($row_data3["dateadmission"]));
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