-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 09, 2022 at 09:31 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1faceattendancedbrfid`
--

-- --------------------------------------------------------

--
-- Table structure for table `attentb`
--

CREATE TABLE `attentb` (
  `id` bigint(250) NOT NULL auto_increment,
  `Date` varchar(250) NOT NULL,
  `Time` varchar(250) NOT NULL,
  `Degree` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `Regno` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `attentb`
--

INSERT INTO `attentb` (`id`, `Date`, `Time`, `Degree`, `Department`, `Year`, `Regno`, `Status`) VALUES
(21, '2022-03-09', '14:55:53', 'UG', 'BE', '2019', '567567', '0');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Regno` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Phone` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Degree` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `RFID` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

