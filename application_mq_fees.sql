-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2024 at 12:30 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `admissionform`
--

-- --------------------------------------------------------

--
-- Table structure for table `application_mq_fees`
--

CREATE TABLE `application_mq_fees` (
  `id` bigint(20) NOT NULL,
  `Year` varchar(100) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Tuition_Fees` varchar(50) NOT NULL,
  `CoExtra_Curricularfees` varchar(50) NOT NULL,
  `Development_fees` varchar(50) NOT NULL,
  `Learning_Materials_Platform_UniformFees` varchar(50) NOT NULL,
  `Caution_Deposit` varchar(50) NOT NULL,
  `Dayscholar` varchar(50) DEFAULT NULL,
  `Hostel` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `application_mq_fees`
--

INSERT INTO `application_mq_fees` (`id`, `Year`, `Department`, `Tuition_Fees`, `CoExtra_Curricularfees`, `Development_fees`, `Learning_Materials_Platform_UniformFees`, `Caution_Deposit`, `Dayscholar`, `Hostel`) VALUES
(1, '2024', 'B.TECH AD', '85000', '50000', '5000', '15000', '5000', NULL, '80000'),
(2, '2024', 'B.E CIVIL', '85000', '50000', '5000', '15000', '5000', NULL, '80000'),
(3, '2024', 'B.TECH CSBS', '85000', '50000', '5000', '15000', '5000', NULL, '80000'),
(4, '2024', 'B.TECH IT', '85000', '50000', '5000', '15000', '5000', NULL, '80000'),
(5, '2024', 'B.E CSE', '87000', '50000', '5000', '15000', '5000', NULL, '80000'),
(6, '2024', 'B.E EEE', '87000', '50000', '5000', '15000', '5000', NULL, '80000'),
(7, '2024', 'B.E ECE', '87000', '50000', '5000', '15000', '5000', NULL, '80000'),
(8, '2024', 'B.E MECH', '87000', '50000', '5000', '15000', '5000', NULL, '80000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `application_mq_fees`
--
ALTER TABLE `application_mq_fees`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `application_mq_fees`
--
ALTER TABLE `application_mq_fees`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
