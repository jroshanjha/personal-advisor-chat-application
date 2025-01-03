CREATE DATABASE  IF NOT EXISTS `learning_model` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `learning_model`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: learning_model
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `progress`
--

DROP TABLE IF EXISTS `progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `progress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `lesson_name` varchar(255) NOT NULL,
  `score` int NOT NULL,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress`
--

LOCK TABLES `progress` WRITE;
/*!40000 ALTER TABLE `progress` DISABLE KEYS */;
INSERT INTO `progress` VALUES (1,'user_1','Lesson_1',5,'2024-12-30 09:13:22'),(2,'user_2','Lesson_2',10,'2024-12-30 09:13:22'),(3,'user_3','Lesson_3',15,'2024-12-30 09:13:22'),(4,'user_4','Lesson_4',20,'2024-12-30 09:13:22'),(5,'user_5','Lesson_5',25,'2024-12-30 09:13:22'),(6,'user_6','Lesson_6',30,'2024-12-30 09:13:22'),(7,'user_7','Lesson_7',35,'2024-12-30 09:13:22'),(8,'user_8','Lesson_8',40,'2024-12-30 09:13:22'),(9,'user_9','Lesson_9',45,'2024-12-30 09:13:22'),(10,'user_10','Lesson_10',50,'2024-12-30 09:13:22'),(11,'user_11','Lesson_11',55,'2024-12-30 09:13:22'),(12,'user_12','Lesson_12',60,'2024-12-30 09:13:22'),(13,'user_13','Lesson_13',65,'2024-12-30 09:13:22'),(14,'user_14','Lesson_14',70,'2024-12-30 09:13:22'),(15,'user_15','Lesson_15',75,'2024-12-30 09:13:22'),(16,'user_16','Lesson_16',80,'2024-12-30 09:13:22'),(17,'user_17','Lesson_17',85,'2024-12-30 09:13:22'),(18,'user_18','Lesson_18',90,'2024-12-30 09:13:22'),(19,'user_19','Lesson_19',95,'2024-12-30 09:13:22'),(20,'user_20','Lesson_20',100,'2024-12-30 09:13:22'),(21,'user_21','Lesson_21',7,'2024-12-30 09:15:29'),(22,'user_22','Lesson_22',14,'2024-12-30 09:15:29'),(23,'user_23','Lesson_23',21,'2024-12-30 09:15:29'),(24,'user_24','Lesson_24',28,'2024-12-30 09:15:29'),(25,'user_25','Lesson_25',35,'2024-12-30 09:15:29'),(26,'user_26','Lesson_26',42,'2024-12-30 09:15:29'),(27,'user_27','Lesson_27',49,'2024-12-30 09:15:29'),(28,'user_28','Lesson_28',56,'2024-12-30 09:15:29'),(29,'user_29','Lesson_29',63,'2024-12-30 09:15:29'),(30,'user_30','Lesson_30',70,'2024-12-30 09:15:29'),(31,'user_31','Lesson_31',77,'2024-12-30 09:15:29'),(32,'user_32','Lesson_32',84,'2024-12-30 09:15:29'),(33,'user_33','Lesson_33',91,'2024-12-30 09:15:29'),(34,'user_34','Lesson_34',98,'2024-12-30 09:15:29'),(35,'user_35','Lesson_35',105,'2024-12-30 09:15:29'),(36,'user_36','Lesson_36',112,'2024-12-30 09:15:29'),(37,'user_37','Lesson_37',119,'2024-12-30 09:15:29'),(38,'user_38','Lesson_38',126,'2024-12-30 09:15:29'),(39,'user_39','Lesson_39',133,'2024-12-30 09:15:29'),(40,'user_40','Lesson_40',140,'2024-12-30 09:15:29'),(41,'user_41','Lesson_41',5,'2024-12-30 09:17:45'),(42,'user_42','Lesson_42',10,'2024-12-30 09:17:45'),(43,'user_43','Lesson_43',15,'2024-12-30 09:17:45'),(44,'user_44','Lesson_44',20,'2024-12-30 09:17:45'),(45,'user_45','Lesson_45',25,'2024-12-30 09:17:45'),(46,'user_46','Lesson_46',30,'2024-12-30 09:17:45'),(47,'user_47','Lesson_47',35,'2024-12-30 09:17:45'),(48,'user_48','Lesson_48',40,'2024-12-30 09:17:45'),(49,'user_49','Lesson_49',45,'2024-12-30 09:17:45'),(50,'user_50','Lesson_50',50,'2024-12-30 09:17:45'),(51,'user_51','Lesson_51',55,'2024-12-30 09:17:45'),(52,'user_52','Lesson_52',60,'2024-12-30 09:17:45'),(53,'user_53','Lesson_53',65,'2024-12-30 09:17:45'),(54,'user_54','Lesson_54',70,'2024-12-30 09:17:45'),(55,'user_55','Lesson_55',75,'2024-12-30 09:17:45'),(56,'user_56','Lesson_56',80,'2024-12-30 09:17:45'),(57,'user_57','Lesson_57',85,'2024-12-30 09:17:45'),(58,'user_58','Lesson_58',90,'2024-12-30 09:17:45'),(59,'user_59','Lesson_59',95,'2024-12-30 09:17:45'),(60,'user_60','Lesson_60',100,'2024-12-30 09:17:45'),(61,'user_61','Lesson_61',7,'2024-12-30 09:18:00'),(62,'user_62','Lesson_62',14,'2024-12-30 09:18:00'),(63,'user_63','Lesson_63',21,'2024-12-30 09:18:00'),(64,'user_64','Lesson_64',28,'2024-12-30 09:18:00'),(65,'user_65','Lesson_65',35,'2024-12-30 09:18:00'),(66,'user_66','Lesson_66',42,'2024-12-30 09:18:00'),(67,'user_67','Lesson_67',49,'2024-12-30 09:18:00'),(68,'user_68','Lesson_68',56,'2024-12-30 09:18:00'),(69,'user_69','Lesson_69',63,'2024-12-30 09:18:00'),(70,'user_70','Lesson_70',70,'2024-12-30 09:18:00'),(71,'user_71','Lesson_71',77,'2024-12-30 09:18:00'),(72,'user_72','Lesson_72',84,'2024-12-30 09:18:00'),(73,'user_73','Lesson_73',91,'2024-12-30 09:18:00'),(74,'user_74','Lesson_74',98,'2024-12-30 09:18:00'),(75,'user_75','Lesson_75',105,'2024-12-30 09:18:00'),(76,'user_76','Lesson_76',112,'2024-12-30 09:18:00'),(77,'user_77','Lesson_77',119,'2024-12-30 09:18:00'),(78,'user_78','Lesson_78',126,'2024-12-30 09:18:00'),(79,'user_79','Lesson_79',133,'2024-12-30 09:18:00'),(80,'user_80','Lesson_80',140,'2024-12-30 09:18:00'),(81,'user_101','Lesson_101',10,'2024-12-30 09:18:44'),(82,'user_102','Lesson_102',20,'2024-12-30 09:18:44'),(83,'user_103','Lesson_103',30,'2024-12-30 09:18:44'),(84,'user_104','Lesson_104',40,'2024-12-30 09:18:44'),(85,'user_105','Lesson_105',50,'2024-12-30 09:18:44'),(86,'user_106','Lesson_106',60,'2024-12-30 09:18:44'),(87,'user_107','Lesson_107',70,'2024-12-30 09:18:44'),(88,'user_108','Lesson_108',80,'2024-12-30 09:18:44'),(89,'user_109','Lesson_109',90,'2024-12-30 09:18:44'),(90,'user_110','Lesson_110',100,'2024-12-30 09:18:44'),(91,'user_111','Lesson_111',110,'2024-12-30 09:18:44'),(92,'user_112','Lesson_112',120,'2024-12-30 09:18:44'),(93,'user_113','Lesson_113',130,'2024-12-30 09:18:44'),(94,'user_114','Lesson_114',140,'2024-12-30 09:18:44'),(95,'user_115','Lesson_115',150,'2024-12-30 09:18:44'),(96,'user_116','Lesson_116',160,'2024-12-30 09:18:44'),(97,'user_117','Lesson_117',170,'2024-12-30 09:18:44'),(98,'user_118','Lesson_118',180,'2024-12-30 09:18:44'),(99,'user_119','Lesson_119',190,'2024-12-30 09:18:44'),(100,'user_120','Lesson_120',200,'2024-12-30 09:18:44'),(101,'user_121','Lesson_121',210,'2024-12-30 09:18:44'),(102,'user_122','Lesson_122',220,'2024-12-30 09:18:44'),(103,'user_123','Lesson_123',230,'2024-12-30 09:18:44'),(104,'user_124','Lesson_124',240,'2024-12-30 09:18:44'),(105,'user_125','Lesson_125',250,'2024-12-30 09:18:44'),(106,'user_126','Lesson_126',260,'2024-12-30 09:18:44'),(107,'user_127','Lesson_127',270,'2024-12-30 09:18:44'),(108,'user_128','Lesson_128',280,'2024-12-30 09:18:44'),(109,'user_129','Lesson_129',290,'2024-12-30 09:18:44'),(110,'user_130','Lesson_130',300,'2024-12-30 09:18:44'),(111,'user_131','Lesson_131',310,'2024-12-30 09:18:44'),(112,'user_132','Lesson_132',320,'2024-12-30 09:18:44'),(113,'user_133','Lesson_133',330,'2024-12-30 09:18:44'),(114,'user_134','Lesson_134',340,'2024-12-30 09:18:44'),(115,'user_135','Lesson_135',350,'2024-12-30 09:18:44'),(116,'user_136','Lesson_136',360,'2024-12-30 09:18:44'),(117,'user_137','Lesson_137',370,'2024-12-30 09:18:44'),(118,'user_138','Lesson_138',380,'2024-12-30 09:18:44'),(119,'user_139','Lesson_139',390,'2024-12-30 09:18:44'),(120,'user_140','Lesson_140',400,'2024-12-30 09:18:44'),(121,'user_141','Lesson_141',410,'2024-12-30 09:18:44'),(122,'user_142','Lesson_142',420,'2024-12-30 09:18:44'),(123,'user_143','Lesson_143',430,'2024-12-30 09:18:44'),(124,'user_144','Lesson_144',440,'2024-12-30 09:18:44'),(125,'user_145','Lesson_145',450,'2024-12-30 09:18:44'),(126,'user_146','Lesson_146',460,'2024-12-30 09:18:44'),(127,'user_147','Lesson_147',470,'2024-12-30 09:18:44'),(128,'user_148','Lesson_148',480,'2024-12-30 09:18:44'),(129,'user_149','Lesson_149',490,'2024-12-30 09:18:44'),(130,'user_150','Lesson_150',500,'2024-12-30 09:18:44'),(131,'admin_user','Introduction',95,'2024-12-30 09:21:39'),(132,'guest_user','Basics of Python',80,'2024-12-30 09:21:39'),(133,'user_1','Advanced SQL',85,'2024-12-30 09:21:39'),(134,'user_2','Web Development',90,'2024-12-30 09:21:39'),(135,'admin_user','Introduction',89,'2024-12-30 09:32:44'),(136,'guest_user','Basics of Python',80,'2024-12-30 09:32:44'),(137,'user_1','Advanced SQL',84,'2024-12-30 09:32:44'),(138,'user_2','Web Development',89,'2024-12-30 09:32:44'),(139,'jroshan','Data Science',76,'2024-12-30 09:32:44'),(140,'programmer123','Python Advanced',58,'2024-12-30 09:32:44'),(141,'user_1','Advanced SQL',45,'2024-12-30 09:32:44'),(142,'user_2','Frontend',690,'2024-12-30 09:32:44'),(143,'system_admin','Networking',79,'2024-12-30 09:32:44'),(144,'tution98','Basics of Python',70,'2024-12-30 09:32:44'),(145,'user_1','Advanced SQL',95,'2024-12-30 09:32:44'),(146,'user_2','Backend',90,'2024-12-30 09:32:44'),(147,'admin_user','Introduction',89,'2024-12-30 10:15:05'),(148,'guest_user','Basics of Python',80,'2024-12-30 10:15:05'),(149,'user_1','Advanced SQL',84,'2024-12-30 10:15:05'),(150,'user_2','Web Development',89,'2024-12-30 10:15:05'),(151,'jroshan','Data Science',76,'2024-12-30 10:15:05'),(152,'programmer123','Python Advanced',58,'2024-12-30 10:15:05'),(153,'user_1','Advanced SQL',45,'2024-12-30 10:15:05'),(154,'user_2','Frontend',690,'2024-12-30 10:15:05'),(155,'system_admin','Networking',79,'2024-12-30 10:15:05'),(156,'tution98','Basics of Python',70,'2024-12-30 10:15:05'),(157,'user_1','Advanced SQL',95,'2024-12-30 10:15:05'),(158,'user_2','Backend',90,'2024-12-30 10:15:05'),(159,'101','DSA for Data science',8,'2024-12-31 11:36:33'),(160,'programmer_123','machine learning ',88,'2025-01-02 10:17:24');
/*!40000 ALTER TABLE `progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user_1','$2b$12$tGdV3pgTHhoIhMa9fTIEnOvScurxROFN7P3DZ91pf/LvIGKpqayA2','2024-12-30 10:22:29'),(2,'testing','$2b$12$vIptAAxMrCG2Xw9NdftkcuMoiaUBdBBFm6vF8getRWkTiOJtRgaL6','2024-12-31 12:20:49'),(3,'programmer_123','$2b$12$Q5tdivUfiGeSMPZr09xjqumYcJHBAclA7JTocfSmD4GUdVLc9FhLe','2024-12-31 12:40:40'),(4,'testing1','$2b$12$IQBVNStHD24SkFL2BbFVTO1dzeS3x4587oOnCZ.9wlX3fOHBD7iDS','2025-01-02 14:06:13');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-03 15:43:33
