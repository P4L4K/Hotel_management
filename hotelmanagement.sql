-- MySQL dump 10.13  Distrib 5.1.73, for Win64 (unknown)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	5.1.73-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customerdetails`
--

DROP TABLE IF EXISTS `customerdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customerdetails` (
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `mobileno` varchar(10) DEFAULT NULL,
  `checkin` date DEFAULT NULL,
  `checkout` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerdetails`
--

LOCK TABLES `customerdetails` WRITE;
/*!40000 ALTER TABLE `customerdetails` DISABLE KEYS */;
INSERT INTO `customerdetails` VALUES ('Ajay singh','Greater Noida','9764584284','2020-10-02','2020-10-06'),('Mr.Khanna','DARYA GANJ','9842584284','2020-05-22','2020-05-20'),('Kunal Thakur','Agra','9764853454','2021-11-02','2021-11-03'),('Adity singh','Ghandhinagar Gujarat','7009453475','2021-12-12','2021-12-16'),('Neha Chauhan ','Mumbai','7006432367','2022-01-02','2022-01-05'),('taniya','shimla','9864353536','2022-02-01','2022-02-03'),('rajeev','gujarat','8876775564','2022-02-14','2022-02-19'),('tanvi sharma','J&K','8786673345','2021-04-20','2021-04-25'),('harsh sinha','NEW DELHI','9567466578','2022-03-01','2022-03-05'),('geeta','shimla','8877559485','2022-02-01','2022-02-04'),('kavita','himachal pradesh','7898834507','2020-03-20','2020-03-24'),('gunjan khanna','delhi','7878834566','2021-04-05','2021-04-08');
/*!40000 ALTER TABLE `customerdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employs`
--

DROP TABLE IF EXISTS `employs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employs` (
  `employID` varchar(25) DEFAULT NULL,
  `employname` varchar(25) DEFAULT NULL,
  `department` varchar(25) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `contactno` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employs`
--

LOCK TABLES `employs` WRITE;
/*!40000 ALTER TABLE `employs` DISABLE KEYS */;
INSERT INTO `employs` VALUES ('111','Rohan guta','accounts',15000,'9586396386'),('122','rita Mahajan','manager',50000,'8953862583'),('105','Mohit gupta','housekeeping',10000,'9678453486'),('112','Mohini Rawat','accounts',15000,'7096858564'),('101','Jyoty Roy','security',10000,'9585688386'),('138','Rohan chauhan','restaurant',18000,'8765396386'),('141','Aryan khan','games',12000,'8953769275'),('108','Tarun Mahajan','houskeeping',10000,'9875478344'),('145','Karan sharma','security',15000,'7794569565'),('102','Sunita guta','laundary',5000,'7695386386'),('125','Kareena khan','receptionist',20000,'7895346546'),('135','rita gupta','laundary',15000,'9876675985'),('104','KRITIKA ','laundary',10000,'8977676555'),('136','Manjeet Babbar','restaurant',16000,'7788546321'),('109','karan','housekeeping',12000,'8899765443'),('139','rohit sharma','restaurant',18000,'7874556478');
/*!40000 ALTER TABLE `employs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game` (
  `sno` int(11) DEFAULT NULL,
  `gamename` varchar(50) DEFAULT NULL,
  `charges` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (1,'Badminton',60),(2,'hockey',90),(3,'cricket',90),(4,'volley ball',60);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laundary`
--

DROP TABLE IF EXISTS `laundary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `laundary` (
  `sno` int(11) DEFAULT NULL,
  `itemname` varchar(50) DEFAULT NULL,
  `rate` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laundary`
--

LOCK TABLES `laundary` WRITE;
/*!40000 ALTER TABLE `laundary` DISABLE KEYS */;
INSERT INTO `laundary` VALUES (1,'shirt',60),(2,'Trouser',80),(3,'ladies suit',100),(4,'saree',120),(5,'other',160);
/*!40000 ALTER TABLE `laundary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant` (
  `sno` int(11) DEFAULT NULL,
  `item` varchar(50) DEFAULT NULL,
  `rate` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant`
--

LOCK TABLES `restaurant` WRITE;
/*!40000 ALTER TABLE `restaurant` DISABLE KEYS */;
INSERT INTO `restaurant` VALUES (1,'sandwich',50),(2,'pizza',120),(3,'samosa',35),(4,'coffee',30),(5,'paneer tikka',90);
/*!40000 ALTER TABLE `restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roomtype`
--

DROP TABLE IF EXISTS `roomtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roomtype` (
  `sno` int(11) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `rent` int(11) DEFAULT NULL,
  `totalrooms` int(11) DEFAULT NULL,
  `availability` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roomtype`
--

LOCK TABLES `roomtype` WRITE;
/*!40000 ALTER TABLE `roomtype` DISABLE KEYS */;
INSERT INTO `roomtype` VALUES (1,'single',2000,10,4),(2,'double',3200,8,5),(3,'triple',4200,10,6),(4,'king',6500,5,2);
/*!40000 ALTER TABLE `roomtype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-15  0:33:43
