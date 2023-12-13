CREATE DATABASE  IF NOT EXISTS `superestrellas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `superestrellas`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: superestrellas
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add actividad',6,'add_actividad'),(22,'Can change actividad',6,'change_actividad'),(23,'Can delete actividad',6,'delete_actividad'),(24,'Can view actividad',6,'view_actividad'),(25,'Can add genero',7,'add_genero'),(26,'Can change genero',7,'change_genero'),(27,'Can delete genero',7,'delete_genero'),(28,'Can view genero',7,'view_genero'),(29,'Can add rol',8,'add_rol'),(30,'Can change rol',8,'change_rol'),(31,'Can delete rol',8,'delete_rol'),(32,'Can view rol',8,'view_rol'),(33,'Can add vinculo familiar',9,'add_vinculofamiliar'),(34,'Can change vinculo familiar',9,'change_vinculofamiliar'),(35,'Can delete vinculo familiar',9,'delete_vinculofamiliar'),(36,'Can view vinculo familiar',9,'view_vinculofamiliar'),(37,'Can add Usuario',10,'add_usuario'),(38,'Can change Usuario',10,'change_usuario'),(39,'Can delete Usuario',10,'delete_usuario'),(40,'Can view Usuario',10,'view_usuario'),(41,'Can add Puntuación de Usuario',11,'add_puntuacionusuario'),(42,'Can change Puntuación de Usuario',11,'change_puntuacionusuario'),(43,'Can delete Puntuación de Usuario',11,'delete_puntuacionusuario'),(44,'Can view Puntuación de Usuario',11,'view_puntuacionusuario'),(45,'Can add inscripcion',12,'add_inscripcion'),(46,'Can change inscripcion',12,'change_inscripcion'),(47,'Can delete inscripcion',12,'delete_inscripcion'),(48,'Can view inscripcion',12,'view_inscripcion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_actividad`
--

DROP TABLE IF EXISTS `core_actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_actividad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `dificultad` varchar(20) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `puntuacion_maxima` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_actividad`
--

LOCK TABLES `core_actividad` WRITE;
/*!40000 ALTER TABLE `core_actividad` DISABLE KEYS */;
INSERT INTO `core_actividad` VALUES (1,'actividad1','Calculadora del ahorro','facil','actividades/Fondo12_5zxIU5w.jpeg',1000),(2,'actividad2','Tienda Virtual','intermedio','actividades/Actividad2Fondo_5f6uUSA.jpeg',1000),(3,'actividad3','Alcancia Magica','facil','actividades/Actividad3Fondo_06E7EyP.jpeg',100),(4,'actividad4','Historia Interactiva','facil','actividades/Fondo3.jpeg',200),(7,'actividad5','Videos','alta','actividades/Actividad2Fondo_ZT4wD94.jpeg',100),(8,'actividad6','Videos','intermedio','actividades/Actividad2Fondo_wF3v0yQ.jpeg',100),(9,'actividad7','Videos','alta','actividades/Actividad3Fondo_47QOPoa.jpeg',100);
/*!40000 ALTER TABLE `core_actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_genero`
--

DROP TABLE IF EXISTS `core_genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_genero` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_genero` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_genero` (`tipo_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_genero`
--

LOCK TABLES `core_genero` WRITE;
/*!40000 ALTER TABLE `core_genero` DISABLE KEYS */;
INSERT INTO `core_genero` VALUES (2,'Femenino'),(3,'Masculino'),(1,'Otro');
/*!40000 ALTER TABLE `core_genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_inscripcion`
--

DROP TABLE IF EXISTS `core_inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_inscripcion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `actividad_id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Core_inscripcion_actividad_id_6277ce46_fk_Core_actividad_id` (`actividad_id`),
  KEY `Core_inscripcion_usuario_id_af5d46df_fk_Core_usuario_id` (`usuario_id`),
  CONSTRAINT `Core_inscripcion_actividad_id_6277ce46_fk_Core_actividad_id` FOREIGN KEY (`actividad_id`) REFERENCES `core_actividad` (`id`),
  CONSTRAINT `Core_inscripcion_usuario_id_af5d46df_fk_Core_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `core_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_inscripcion`
--

LOCK TABLES `core_inscripcion` WRITE;
/*!40000 ALTER TABLE `core_inscripcion` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_inscripcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_puntuacionusuario`
--

DROP TABLE IF EXISTS `core_puntuacionusuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_puntuacionusuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `puntuacion` int NOT NULL,
  `fecha_ganado` datetime(6) NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `Core_puntuacionusuario_usuario_id_12273bb9_fk_Core_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `core_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_puntuacionusuario`
--

LOCK TABLES `core_puntuacionusuario` WRITE;
/*!40000 ALTER TABLE `core_puntuacionusuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_puntuacionusuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_rol`
--

DROP TABLE IF EXISTS `core_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_rol` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_usuario` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_rol`
--

LOCK TABLES `core_rol` WRITE;
/*!40000 ALTER TABLE `core_rol` DISABLE KEYS */;
INSERT INTO `core_rol` VALUES (1,'Padre'),(2,'Niño');
/*!40000 ALTER TABLE `core_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_usuario`
--

DROP TABLE IF EXISTS `core_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `puntuacion` int NOT NULL,
  `codigo_unico` varchar(6) DEFAULT NULL,
  `estado` varchar(15) NOT NULL,
  `limite_vinculos` int NOT NULL,
  `genero_id` bigint DEFAULT NULL,
  `rol_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `codigo_unico` (`codigo_unico`),
  KEY `Core_usuario_genero_id_63d23dde_fk_Core_genero_id` (`genero_id`),
  KEY `Core_usuario_rol_id_6a99aa36_fk_Core_rol_id` (`rol_id`),
  CONSTRAINT `Core_usuario_genero_id_63d23dde_fk_Core_genero_id` FOREIGN KEY (`genero_id`) REFERENCES `core_genero` (`id`),
  CONSTRAINT `Core_usuario_rol_id_6a99aa36_fk_Core_rol_id` FOREIGN KEY (`rol_id`) REFERENCES `core_rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_usuario`
--

LOCK TABLES `core_usuario` WRITE;
/*!40000 ALTER TABLE `core_usuario` DISABLE KEYS */;
INSERT INTO `core_usuario` VALUES (1,'2023-12-13 07:44:45.044724',1,'',1,1,'2023-12-11 08:40:22.466570','pbkdf2_sha256$600000$XxRUyDpELTZVLF6TiLRLAz$hoPxJeB31E+hF6lKiNMIVYbNZfcCGOBPQZOUd1TrrdU=','Admin',NULL,NULL,'Admin@gmail.com',100,'738146','Habilitado',1,NULL,NULL),(6,'2023-12-11 09:24:02.207665',0,'Acosta',0,1,'2023-12-11 09:23:35.700886','pbkdf2_sha256$600000$ZrHCgdWLx3SA2dIcZGPQaH$nReL/bW0HZ3J+D1hOS5S7ZfT4v4t5Fl75HARbuGO8xs=','Julian12','Julian David','Acosta','Juli12@gmail.com',0,'336211','Habilitado',1,3,2),(7,'2023-12-11 13:06:26.915565',0,'Gomez',0,1,'2023-12-11 09:26:11.242639','pbkdf2_sha256$600000$tfbta3S6YfKq1sFRWfx5Zr$xuJm3ptLbJBL3ubbYkt9WoZ2ItXfxCKupbdhQKKb+P4=','Sarita10','Sara Sofia','Gomez','Sofy@gmail.com',132,'679932','Habilitado',1,2,2),(8,'2023-12-11 12:07:57.320883',0,'Acosta',0,1,'2023-12-11 09:29:05.830877','pbkdf2_sha256$600000$uiB8d9cQqMMIkC8wg0FsNE$hnyk01lhrBR+dgKvDKnF9SYaK8WxdhB0+QHNmJT37kI=','Jhonny78','Jhonny Alexander','Acosta','brayanacostamesa@gmail.com',0,'139520','Habilitado',1,3,1),(9,'2023-12-11 11:54:27.859748',0,'Gomez',0,1,'2023-12-11 09:32:02.030250','pbkdf2_sha256$600000$D2oic51SJLNnlltNbYjSYX$PiGKHzZqyNkpuU6RmjjWDX6WZcsv4A+Z0kfv/4a0OmU=','Maria10','Maria Helena','Gomez','Maria10@gmail.com',0,'915156','Habilitado',1,2,1),(10,'2023-12-11 12:58:52.472092',0,'Velasquez',0,1,'2023-12-11 12:51:11.204577','pbkdf2_sha256$600000$iBNz2ScvAFfkSPbfsOxH07$daBFo4iE3uz0eLv0PESxqqWy9L/9wvBCs4q1HkehoNA=','Erick','Erick','Velasquez','Erick@gmail.com',0,'455984','Habilitado',1,3,1),(11,NULL,0,'Velasquez',0,1,'2023-12-11 12:51:53.521846','pbkdf2_sha256$600000$n1UjgkTGK6cCJnFcFDaQlU$vQAM0onZoBCmOjC2ZqkVuU8kQ0DJDsBwhY+VtGcnAt8=','Yesid','Yesid','Velasquez','Yesid@gmail.com',0,'852319','Habilitado',1,3,2),(12,'2023-12-13 07:43:05.647693',0,'Ramirez',0,1,'2023-12-13 04:52:41.321213','pbkdf2_sha256$600000$wqD5UOjHtXqbEiVlfayRis$5oqQ7ZaactKzrNnbZ4oKxZZXY9j62ed/WtdF0MDVp04=','Oscar_27','Oscar','Ramirez','oscar27@hotmail.com',0,'387192','Habilitado',1,3,1),(13,NULL,0,'Ramirez',0,1,'2023-12-13 04:54:27.862746','pbkdf2_sha256$600000$fypMEwSGzCpx7XLkh2IyVm$33Ld2Xno+WL5Oqr4aSKGeSljTjc+XnKtmA3OouhWPM4=','Emma.27','Emma','Ramirez','Emma27@hotmail.com',0,'487853','Habilitado',1,2,2);
/*!40000 ALTER TABLE `core_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_usuario_actividades_inscritas`
--

DROP TABLE IF EXISTS `core_usuario_actividades_inscritas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_usuario_actividades_inscritas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `actividad_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Core_usuario_actividades_usuario_id_actividad_id_d9e9cabc_uniq` (`usuario_id`,`actividad_id`),
  KEY `Core_usuario_activid_actividad_id_796cbc5f_fk_Core_acti` (`actividad_id`),
  CONSTRAINT `Core_usuario_activid_actividad_id_796cbc5f_fk_Core_acti` FOREIGN KEY (`actividad_id`) REFERENCES `core_actividad` (`id`),
  CONSTRAINT `Core_usuario_activid_usuario_id_d9e59986_fk_Core_usua` FOREIGN KEY (`usuario_id`) REFERENCES `core_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_usuario_actividades_inscritas`
--

LOCK TABLES `core_usuario_actividades_inscritas` WRITE;
/*!40000 ALTER TABLE `core_usuario_actividades_inscritas` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_usuario_actividades_inscritas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_usuario_groups`
--

DROP TABLE IF EXISTS `core_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Core_usuario_groups_usuario_id_group_id_67c8ec38_uniq` (`usuario_id`,`group_id`),
  KEY `Core_usuario_groups_group_id_08897db7_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Core_usuario_groups_group_id_08897db7_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `Core_usuario_groups_usuario_id_e3f9fc85_fk_Core_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `core_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_usuario_groups`
--

LOCK TABLES `core_usuario_groups` WRITE;
/*!40000 ALTER TABLE `core_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_usuario_user_permissions`
--

DROP TABLE IF EXISTS `core_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Core_usuario_user_permis_usuario_id_permission_id_f2cedb4c_uniq` (`usuario_id`,`permission_id`),
  KEY `Core_usuario_user_pe_permission_id_144ffa5b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Core_usuario_user_pe_permission_id_144ffa5b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `Core_usuario_user_pe_usuario_id_8259c52f_fk_Core_usua` FOREIGN KEY (`usuario_id`) REFERENCES `core_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_usuario_user_permissions`
--

LOCK TABLES `core_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vinculofamiliar`
--

DROP TABLE IF EXISTS `core_vinculofamiliar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_vinculofamiliar` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_principal_id` bigint NOT NULL,
  `usuario_vinculado_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Core_vinculofamiliar_usuario_principal_id_f184627b_fk_Core_usua` (`usuario_principal_id`),
  KEY `Core_vinculofamiliar_usuario_vinculado_id_04179f3a_fk_Core_usua` (`usuario_vinculado_id`),
  CONSTRAINT `Core_vinculofamiliar_usuario_principal_id_f184627b_fk_Core_usua` FOREIGN KEY (`usuario_principal_id`) REFERENCES `core_usuario` (`id`),
  CONSTRAINT `Core_vinculofamiliar_usuario_vinculado_id_04179f3a_fk_Core_usua` FOREIGN KEY (`usuario_vinculado_id`) REFERENCES `core_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vinculofamiliar`
--

LOCK TABLES `core_vinculofamiliar` WRITE;
/*!40000 ALTER TABLE `core_vinculofamiliar` DISABLE KEYS */;
INSERT INTO `core_vinculofamiliar` VALUES (1,9,7),(3,10,11);
/*!40000 ALTER TABLE `core_vinculofamiliar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Core_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Core_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `core_usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-11 08:41:21.929498','1','Otro',1,'[{\"added\": {}}]',7,1),(2,'2023-12-11 08:41:24.976970','2','Femenino',1,'[{\"added\": {}}]',7,1),(3,'2023-12-11 08:41:28.686095','3','Masculino',1,'[{\"added\": {}}]',7,1),(4,'2023-12-11 08:50:57.535434','2','Brayan25',3,'',10,1),(5,'2023-12-11 08:50:57.541399','3','pepe',3,'',10,1),(6,'2023-12-11 09:21:32.241042','4','Erick',3,'',10,1),(7,'2023-12-11 09:21:32.247123','5','Erick1',3,'',10,1),(8,'2023-12-11 09:36:42.227481','1','actividad1 (Puntuación Máxima: 1000)',1,'[{\"added\": {}}]',6,1),(9,'2023-12-11 09:37:15.075929','2','actividad2 (Puntuación Máxima: 1000)',1,'[{\"added\": {}}]',6,1),(10,'2023-12-11 09:37:53.220708','3','actividad3 (Puntuación Máxima: 100)',1,'[{\"added\": {}}]',6,1),(11,'2023-12-11 09:38:34.711318','4','actividad4 (Puntuación Máxima: 200)',1,'[{\"added\": {}}]',6,1),(12,'2023-12-11 12:58:18.251468','2','Erick - Yesid',3,'',9,1),(13,'2023-12-11 13:10:45.100900','5','actividad5 (Puntuación Máxima: 100)',1,'[{\"added\": {}}]',6,1),(14,'2023-12-11 13:14:16.864146','5','actividad5 (Puntuación Máxima: 100)',3,'',6,1),(15,'2023-12-11 13:14:32.150003','6','actividad5 (Puntuación Máxima: 100)',1,'[{\"added\": {}}]',6,1),(16,'2023-12-11 13:16:34.547704','6','actividad5 (Puntuación Máxima: 100)',3,'',6,1),(17,'2023-12-11 13:17:00.910032','7','actividad5 (Puntuación Máxima: 100)',1,'[{\"added\": {}}]',6,1),(18,'2023-12-11 13:17:44.315798','8','actividad6 (Puntuación Máxima: 100)',1,'[{\"added\": {}}]',6,1),(19,'2023-12-11 13:18:09.178960','9','actividad7 (Puntuación Máxima: 100)',1,'[{\"added\": {}}]',6,1),(20,'2023-12-13 05:46:20.225707','4','Oscar_27 - Emma.27',3,'',9,1),(21,'2023-12-13 06:06:31.183927','5','Oscar_27 - Emma.27',3,'',9,1),(22,'2023-12-13 06:19:14.837878','6','Oscar_27 - Emma.27',3,'',9,1),(23,'2023-12-13 07:42:42.100266','7','Oscar_27 - Emma.27',3,'',9,1),(24,'2023-12-13 07:44:51.453251','8','Oscar_27 - Emma.27',3,'',9,1),(25,'2023-12-13 07:56:25.628069','9','Admin - Emma.27',3,'',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'Core','actividad'),(7,'Core','genero'),(12,'Core','inscripcion'),(11,'Core','puntuacionusuario'),(8,'Core','rol'),(10,'Core','usuario'),(9,'Core','vinculofamiliar'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-11 08:39:45.924441'),(2,'contenttypes','0002_remove_content_type_name','2023-12-11 08:39:46.069906'),(3,'auth','0001_initial','2023-12-11 08:39:46.454153'),(4,'auth','0002_alter_permission_name_max_length','2023-12-11 08:39:46.534775'),(5,'auth','0003_alter_user_email_max_length','2023-12-11 08:39:46.542775'),(6,'auth','0004_alter_user_username_opts','2023-12-11 08:39:46.550069'),(7,'auth','0005_alter_user_last_login_null','2023-12-11 08:39:46.557070'),(8,'auth','0006_require_contenttypes_0002','2023-12-11 08:39:46.562075'),(9,'auth','0007_alter_validators_add_error_messages','2023-12-11 08:39:46.569969'),(10,'auth','0008_alter_user_username_max_length','2023-12-11 08:39:46.578609'),(11,'auth','0009_alter_user_last_name_max_length','2023-12-11 08:39:46.585613'),(12,'auth','0010_alter_group_name_max_length','2023-12-11 08:39:46.605612'),(13,'auth','0011_update_proxy_permissions','2023-12-11 08:39:46.615619'),(14,'auth','0012_alter_user_first_name_max_length','2023-12-11 08:39:46.625622'),(15,'Core','0001_initial','2023-12-11 08:39:48.293370'),(16,'admin','0001_initial','2023-12-11 08:39:48.528460'),(17,'admin','0002_logentry_remove_auto_add','2023-12-11 08:39:48.540470'),(18,'admin','0003_logentry_add_action_flag_choices','2023-12-11 08:39:48.551472'),(19,'sessions','0001_initial','2023-12-11 08:39:48.606793');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('shdvantqx59vjnmb88v0cotnrm082zlc','.eJxVjEEOwiAQRe_C2pCZFpzBpXvPQBhAqRpISrsy3l2bdKHb_977L-XDuhS_9jz7KamTQnX43STER64bSPdQb03HVpd5Er0peqddX1rKz_Pu_h2U0Mu3JmvGEQQJk0E0RIYCREIYmIejC2yRkdg6EIdZorNELOQsQL6CJPX-AIlENfs:1rDID5:PO0v-SFkHV9_ZLJDziZSRVHxj6L9xebYlDh5CGAZjsM','2023-12-27 05:55:07.647578'),('v48ss8q5pi09j2657lu33naeeij19rus','.eJxVjEEOwiAQRe_C2pCZFpzBpXvPQBhAqRpISrsy3l2bdKHb_977L-XDuhS_9jz7KamTQnX43STER64bSPdQb03HVpd5Er0peqddX1rKz_Pu_h2U0Mu3JmvGEQQJk0E0RIYCREIYmIejC2yRkdg6EIdZorNELOQsQL6CJPX-AIlENfs:1rDJvB:rxdOYMiXs51zOkdcEkiI03Kezj8KksZOXPSyVt3JYXg','2023-12-27 07:44:45.049533');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-13  9:50:09
