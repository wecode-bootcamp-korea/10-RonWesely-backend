-- MySQL dump 10.13  Distrib 8.0.19, for osx10.15 (x86_64)
--
-- Host: localhost    Database: wiselydb
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blade_products`
--

DROP TABLE IF EXISTS `blade_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blade_products` (`id` int NOT NULL AUTO_INCREMENT, `price` decimal(10,2) NOT NULL,`product_id` int DEFAULT NULL, PRIMARY KEY (`id`), KEY `blade_products_product_id_e973e384_fk_products_id` (`product_id`),CONSTRAINT `blade_products_product_id_e973e384_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blade_products`
--

LOCK TABLES `blade_products` WRITE;
/*!40000 ALTER TABLE `blade_products` DISABLE KEYS */;
INSERT INTO `blade_products` VALUES (1,100.00,1),(2,200.00,1),(3,300.00,1),(4,400.00,1),(5,500.00,1);
/*!40000 ALTER TABLE `blade_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colors`
--

DROP TABLE IF EXISTS `colors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colors` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(20) NOT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colors`
--

LOCK TABLES `colors` WRITE;
/*!40000 ALTER TABLE `colors` DISABLE KEYS */;
INSERT INTO `colors` VALUES (1,'미드나이트 네이비'),(2,'사파이어 블루'),(3,'슬레이트 그레이');
/*!40000 ALTER TABLE `colors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (`id` int NOT NULL AUTO_INCREMENT,`app_label` varchar(100) NOT NULL,`model` varchar(100) NOT NULL,PRIMARY KEY (`id`),UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(11,'orders','order'),(8,'orders','orderimage'),(9,'orders','orderitem'),(12,'orders','orderstatus'),(10,'orders','review'),(17,'products','bladeproduct'),(14,'products','color'),(13,'products','product'),(16,'products','productcolor'),(19,'products','productsize'),(18,'products','size'),(15,'products','skintype'),(2,'sessions','session'),(4,'users','gender'),(5,'users','path'),(7,'users','path_result'),(6,'users','shipping'),(3,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (`id` int NOT NULL AUTO_INCREMENT,`app` varchar(255) NOT NULL,`name` varchar(255) NOT NULL,`applied` datetime(6) NOT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-07-23 08:48:01.206911'),(2,'contenttypes','0002_remove_content_type_name','2020-07-23 08:48:01.232511'),(3,'sessions','0001_initial','2020-07-23 08:48:01.241282'),(4,'users','0001_initial','2020-07-23 08:48:01.258130'),(5,'users','0002_auto_20200722_1654','2020-07-23 08:48:01.287673'),(6,'users','0003_auto_20200723_1700','2020-07-23 08:48:01.380300'),(7,'users','0004_auto_20200723_1837','2020-07-23 09:37:31.142767'),(8,'users','0002_auto_20200725_1415','2020-07-25 05:15:29.141447'),(9,'products','0001_initial','2020-07-28 12:25:40.854998'),(11,'orders','0001_initial','2020-07-29 06:14:08.985264');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL,`session_data` longtext NOT NULL,`expire_date` datetime(6) NOT NULL,PRIMARY KEY (`session_key`),KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genders`
--

DROP TABLE IF EXISTS `genders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genders` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(10) NOT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genders`
--

LOCK TABLES `genders` WRITE;
/*!40000 ALTER TABLE `genders` DISABLE KEYS */;
INSERT INTO `genders` VALUES (1,'남자'),(2,'여자');
/*!40000 ALTER TABLE `genders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_images`
--

DROP TABLE IF EXISTS `order_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_images` (`id` int NOT NULL AUTO_INCREMENT,`image_url` varchar(1000) NOT NULL,`blade_products_id` int DEFAULT NULL,`products_colors_id` int DEFAULT NULL,`products_sizes_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `order_images_blade_products_id_2bc4f039_fk_blade_products_id` (`blade_products_id`),KEY `order_images_products_colors_id_49e51158_fk_products_colors_id` (`products_colors_id`),KEY `order_images_products_sizes_id_ac60b751_fk_products_sizes_id` (`products_sizes_id`),CONSTRAINT `order_images_blade_products_id_2bc4f039_fk_blade_products_id` FOREIGN KEY (`blade_products_id`) REFERENCES `blade_products` (`id`),CONSTRAINT `order_images_products_colors_id_49e51158_fk_products_colors_id` FOREIGN KEY (`products_colors_id`) REFERENCES `products_colors` (`id`),CONSTRAINT `order_images_products_sizes_id_ac60b751_fk_products_sizes_id` FOREIGN KEY (`products_sizes_id`) REFERENCES `products_sizes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_images`
--

LOCK TABLES `order_images` WRITE;
/*!40000 ALTER TABLE `order_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_items` (`id` int NOT NULL AUTO_INCREMENT,`quantity` int NOT NULL,`discount_price` decimal(10,2) NOT NULL,`blade_products_id` int DEFAULT NULL,`order_id` int DEFAULT NULL,`product_colors_id` int DEFAULT NULL,`product_sizes_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `order_items_blade_products_id_be474d35_fk_blade_products_id` (`blade_products_id`),KEY `order_items_order_id_412ad78b_fk_orders_id` (`order_id`),KEY `order_items_product_colors_id_846fd131_fk_products_colors_id` (`product_colors_id`),KEY `order_items_product_sizes_id_cb70b93c_fk_products_sizes_id` (`product_sizes_id`),CONSTRAINT `order_items_blade_products_id_be474d35_fk_blade_products_id` FOREIGN KEY (`blade_products_id`) REFERENCES `blade_products` (`id`),CONSTRAINT `order_items_order_id_412ad78b_fk_orders_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),CONSTRAINT `order_items_product_colors_id_846fd131_fk_products_colors_id` FOREIGN KEY (`product_colors_id`) REFERENCES `products_colors` (`id`),CONSTRAINT `order_items_product_sizes_id_cb70b93c_fk_products_sizes_id` FOREIGN KEY (`product_sizes_id`) REFERENCES `products_sizes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

LOCK TABLES `order_items` WRITE;
/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
INSERT INTO `order_items` VALUES (1,1,0.00,NULL,1,1,NULL);
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_statuses`
--

DROP TABLE IF EXISTS `order_statuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_statuses` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(10) NOT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_statuses`
--

LOCK TABLES `order_statuses` WRITE;
/*!40000 ALTER TABLE `order_statuses` DISABLE KEYS */;
INSERT INTO `order_statuses` VALUES (1,'pending'),(2,'결제완료');
/*!40000 ALTER TABLE `order_statuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (`id` int NOT NULL AUTO_INCREMENT,`shipping_price` decimal(10,2) NOT NULL,`list_price` decimal(10,2) NOT NULL,`discount_price` decimal(10,2) NOT NULL,`total_price` decimal(10,2) NOT NULL,`created_at` datetime(6) NOT NULL,`ordered_at` datetime(6) DEFAULT NULL,`order_status_id` int DEFAULT NULL,`shipping_id` int DEFAULT NULL,`user_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `orders_order_status_id_05e726df_fk_order_statuses_id` (`order_status_id`),KEY `orders_shipping_id_b3ab186f_fk_shippings_id` (`shipping_id`),KEY `orders_user_id_7e2523fb_fk_users_id` (`user_id`),CONSTRAINT `orders_order_status_id_05e726df_fk_order_statuses_id` FOREIGN KEY (`order_status_id`) REFERENCES `order_statuses` (`id`),CONSTRAINT `orders_shipping_id_b3ab186f_fk_shippings_id` FOREIGN KEY (`shipping_id`) REFERENCES `shippings` (`id`),CONSTRAINT `orders_user_id_7e2523fb_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,0.00,100000.00,10000.00,100000.00,'2020-07-29 08:33:04.000000','2020-07-29 08:33:04.000000',2,1,1),(2,0.00,200000.00,20000.00,200000.00,'2020-07-29 08:33:04.000000','2020-07-29 08:33:04.000000',2,3,2);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `path_results`
--

DROP TABLE IF EXISTS `path_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `path_results` (`id` int NOT NULL AUTO_INCREMENT,`path_lists_id` int DEFAULT NULL,`users_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `path_results_path_lists_id_cbd0941e_fk_paths_id` (`path_lists_id`),KEY `path_results_users_id_58ebc1ae_fk_users_id` (`users_id`),CONSTRAINT `path_results_path_lists_id_cbd0941e_fk_paths_id` FOREIGN KEY (`path_lists_id`) REFERENCES `paths` (`id`),CONSTRAINT `path_results_users_id_58ebc1ae_fk_users_id` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `path_results`
--

LOCK TABLES `path_results` WRITE;
/*!40000 ALTER TABLE `path_results` DISABLE KEYS */;
/*!40000 ALTER TABLE `path_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paths`
--

DROP TABLE IF EXISTS `paths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paths` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paths`
--

LOCK TABLES `paths` WRITE;
/*!40000 ALTER TABLE `paths` DISABLE KEYS */;
/*!40000 ALTER TABLE `paths` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(20) NOT NULL,`description` varchar(50) NOT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'선물세트','건강한 면도 습관을 선물하세요'),(2,'면도기세트','부드럽고 정교한 면도 독일산 5중 면도날'),(3,'리필면도날','당김 없이 편안하게 독일상 5중 면도날'),(4,'셰이빙젤','자극없이 부드러운 면도를 원한다면'),(5,'애프터셰이브','면도의 마무리는 자극받은 피부케어');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_colors`
--

DROP TABLE IF EXISTS `products_colors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_colors` (`id` int NOT NULL AUTO_INCREMENT,`price` decimal(10,2) NOT NULL,`color_id` int DEFAULT NULL,`product_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `products_colors_color_id_6f4711fc_fk_colors_id` (`color_id`),KEY `products_colors_product_id_6c9653b3_fk_products_id` (`product_id`),CONSTRAINT `products_colors_color_id_6f4711fc_fk_colors_id` FOREIGN KEY (`color_id`) REFERENCES `colors` (`id`),CONSTRAINT `products_colors_product_id_6c9653b3_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_colors`
--

LOCK TABLES `products_colors` WRITE;
/*!40000 ALTER TABLE `products_colors` DISABLE KEYS */;
INSERT INTO `products_colors` VALUES (1,100.00,1,1),(2,200.00,2,2),(3,300.00,3,3),(4,400.00,1,4),(5,500.00,2,5);
/*!40000 ALTER TABLE `products_colors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_sizes`
--

DROP TABLE IF EXISTS `products_sizes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_sizes` (`id` int NOT NULL AUTO_INCREMENT,`price` decimal(10,2) NOT NULL,`product_id` int DEFAULT NULL,`size_id` int DEFAULT NULL,`skin_type_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `products_sizes_product_id_2e2d0557_fk_products_id` (`product_id`),KEY `products_sizes_size_id_d19716a2_fk_sizes_id` (`size_id`),KEY `products_sizes_skin_type_id_d1fbc386_fk_skin_types_id` (`skin_type_id`),CONSTRAINT `products_sizes_product_id_2e2d0557_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),CONSTRAINT `products_sizes_size_id_d19716a2_fk_sizes_id` FOREIGN KEY (`size_id`) REFERENCES `sizes` (`id`),CONSTRAINT `products_sizes_skin_type_id_d1fbc386_fk_skin_types_id` FOREIGN KEY (`skin_type_id`) REFERENCES `skin_types` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_sizes`
--

LOCK TABLES `products_sizes` WRITE;
/*!40000 ALTER TABLE `products_sizes` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_sizes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (`id` int NOT NULL AUTO_INCREMENT,`rate` decimal(10,2) NOT NULL,`review_text` varchar(300) NOT NULL,`writed_at` datetime(6) NOT NULL,`order_item_id` int DEFAULT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,5.00,'괜찮았어요^^~~~','2020-07-29 08:33:04.101338',1),(2,5.00,'가성비 최상으로 만족하고 주변에도 추천하고 있습니다.','2020-07-29 08:33:04.105606',1),(3,5.00,'저는 수십년동안 질래트 면도기을 써왔으나 와이즐리로 바꾸어 사용해보니 아주 가성비가 뛰어난 상품이다.\n단 면도기 손잡이가 미끄럽고 조금은 불편하다.','2020-07-29 08:33:04.106789',1),(4,5.00,'기존에 제품과는 거품에 사용감이 달라 너무 좋습니다. 또한 과다하게 사용량이 나오지 않아서 또 좋네요..  아주 실 생활에 딱 안성맞춤이에요..  감사합니다.','2020-07-29 08:33:04.107812',1),(5,5.00,'잘사용하구있구요\n저렴하면서실용적인것갇아요\n좋은제품홍보할개요','2020-07-29 08:33:04.109241',1),(6,5.00,'세상에... 이런 제품을 이제 알았다는게 너무 후회되네요 처음엔 면도날 보호커버 끼고 면도하는줄 알았어요 그래서 보니까 면도날이더군요.. 어마어마한 절삭력과 부드러움 놀라움의 끝입니다.. 질xx 빠이입니다','2020-07-29 08:33:04.109890',1),(7,5.00,'가성비도 괜찮고 제품의 품질이 너무 좋네요 \n앞으로도 잘쓰겠습니다 ㅋㅋ','2020-07-29 08:33:04.110508',1),(8,5.00,'즐거운 아침을 맞이하고 있습니다','2020-07-29 08:33:04.111103',1),(9,5.00,'제품을 받았을때부터 심쿵했는데\n사용하는 중에도 부드럽고 매끄럽게\n깍이는게 기분 좋은 느낌이었습니다.\n애용 하도록 하겠습니다!\n감사합니다 ^^','2020-07-29 08:33:04.111745',1),(10,5.00,'젤이 진짜 좋아요!','2020-07-29 08:33:04.112405',1),(11,1.00,'면도할때자루손잡이가미끄러워서 좀 안좋아요','2020-07-29 08:33:04.112988',1),(12,5.00,'가격대비나쁘진않음.\n엄청좋은데 가격저렴한줄알았지만 확실히 유명브랜드보다\n성능이 떨어지는건 어쩔수없음. (단, 저는 진동면도기를 썼으니 비교자체가 무의미함. 비진동 면도기랑 비교하면 꿀리지않음)\n\n합리적인가격에 이용가능하니 추천할의향있음.\n\n포장 굿. 면도기주제에 라고 생각했지만 이 제품을 만든 분들입장에서는 면도기가 인생일듯. 포장 의외로 너무 고급지고 친절설명까지있어서 대우받는느낌\n\n재구매의향있음','2020-07-29 08:33:04.113520',1),(13,5.00,'남편이 면도기가 너무 좋다고 하나 더 주문해달라네요.','2020-07-29 08:33:04.114630',1),(14,3.00,'절삭력이 조금 더 보강되었으면 해요','2020-07-29 08:33:04.115349',1),(15,5.00,'누군가에게 선물하기좋아요 포장도깔끔하고 받는분도 기분좋을만큼 세련된 느낌^^','2020-07-29 08:33:04.115958',1),(16,5.00,'거품이아닌젤부터가맘에드네요 면도기날도부드럽게잘깍이는게좋네요 면도기디자인도 굿','2020-07-29 08:33:04.116530',1),(17,5.00,'매력적이고 실속있는 구성이 참 좋습니다! 저는 직접 쓸려고 구입 했지만 선물용으로 쓸 수 있게 쇼핑백도 제공해 주시고 패키징도 산뜻하니 아주 맘에 듭니다! 물론 면도기 성능은 수 많은 후기들처럼 기존 브랜드 대비 떨어짐 전혀 없이 좋으니 후회 없는 선택이 될 것 같네요.','2020-07-29 08:33:04.117147',1),(18,5.00,'면도기 본체가 참 좋아요..\n면도날도 깔끔하게 느껴지는 절삭을 하네요~~\n기존사용하던 면도기는 너무 비싼 상품이였네요~\n가성비 좋은 우수한 품질로 변경하기를 잘했습니다','2020-07-29 08:33:04.117766',1),(19,5.00,'일단\n면도를  처음사용 하게되는 아들에게 선물하게\n되어서 좋고 아들이 좋아하니 좋고\n좋은제품을 아들에게 알려줄수 있어서\n좋은것같아요','2020-07-29 08:33:04.118347',1),(20,5.00,'부드럽게 미끄러지는 면도날이 긴장을 풀어 줬습니다','2020-07-29 08:33:04.119004',1),(21,5.00,'가성비가 좋아요\n역쉬 품질이 뛰어나네요\n적극추천합니다 ','2020-07-29 08:33:04.119620',1),(22,5.00,'신랑한테 선물 했는데 젤 타입이라 바를때 느낌이 좋다고 하네요 ','2020-07-29 08:33:04.120843',1),(23,5.00,'가성비끝판왕에 내구성이 엄청남','2020-07-29 08:33:04.121409',1),(24,5.00,'가성비최고면도날도 정말부드러워요!!!!','2020-07-29 08:33:04.121989',1),(25,5.00,'다른 면도기 보다 약간의 무게감도 있고 부드럽게 살같을 면도함. 아주 좋습니다.\n\n좋은 제품을 친구들에게 권하려고 합이다.','2020-07-29 08:33:04.122535',1);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shippings`
--

DROP TABLE IF EXISTS `shippings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shippings` (`id` int NOT NULL AUTO_INCREMENT,`recipient` varchar(10) NOT NULL,`phone_number` varchar(20) NOT NULL,`address` varchar(20) NOT NULL,`address_detail` varchar(100) NOT NULL,`requirement` varchar(100) NOT NULL,`is_default` tinyint(1) NOT NULL,`user_id` int DEFAULT NULL,PRIMARY KEY (`id`),KEY `shippings_user_id_4d31e245_fk_users_id` (`user_id`),CONSTRAINT `shippings_user_id_4d31e245_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shippings`
--

LOCK TABLES `shippings` WRITE;
/*!40000 ALTER TABLE `shippings` DISABLE KEYS */;
INSERT INTO `shippings` VALUES (1,'Alex','010-1234-5678','경기도 의정부시','신곡동','빨리',1,1),(3,'Bobby','010-9876-5432','서울시 강남구','강남역 지하상가','빨리요',1,2);
/*!40000 ALTER TABLE `shippings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sizes`
--

DROP TABLE IF EXISTS `sizes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sizes` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(20) NOT NULL,`description` varchar(10) DEFAULT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sizes`
--

LOCK TABLES `sizes` WRITE;
/*!40000 ALTER TABLE `sizes` DISABLE KEYS */;
INSERT INTO `sizes` VALUES (1,'150ml','스탠다드'),(2,'75ml','여행용');
/*!40000 ALTER TABLE `sizes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skin_types`
--

DROP TABLE IF EXISTS `skin_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skin_types` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(10) NOT NULL,PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skin_types`
--

LOCK TABLES `skin_types` WRITE;
/*!40000 ALTER TABLE `skin_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `skin_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (`id` int NOT NULL AUTO_INCREMENT,`email` varchar(250) NOT NULL,`password` varchar(300) NOT NULL,`phone_number` varchar(20) NOT NULL,`birthday` date NOT NULL,`name` varchar(10) NOT NULL,`gender_type_id` int DEFAULT NULL,`is_notified` tinyint(1) NOT NULL,`created_at` datetime(6) NOT NULL,`modified_at` datetime(6) NOT NULL,PRIMARY KEY (`id`),KEY `users_gender_id_5b939083` (`gender_type_id`),CONSTRAINT `users_gender_type_id_121f9ad7_fk_genders_id` FOREIGN KEY (`gender_type_id`) REFERENCES `genders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'logintest1@naver.com','$2b$12$LrQstf4T5THB0sapEe8D4OLU0RfVskEOng8bwIx8.f5MUx35BA/46','01234567890','1990-02-06','황수미',1,0,'2020-07-23 11:25:19.834074','2020-07-23 11:25:19.835389'),(2,'logintest2@naver.com','$2b$12$zLzK3TMmeNzO0XcXpDozsOKy3/zu7lJP.kHBVSmu4vkF8Lqpyzs52','01234567890','1980-03-02','황수미2',2,0,'2020-07-23 12:20:23.154004','2020-07-23 12:20:23.155094'),(3,'logintest2@aver.com','$2b$12$HL.LvkH6x8tpqYhqkaP7i.IIimbLsP5cfR8iO7UiCGkrjfn4IBmqC','01234567890','1970-03-02','황수미3',2,0,'2020-07-23 13:22:19.006549','2020-07-23 13:22:19.008658'),(4,'logintest2@ver.com','$2b$12$z4DP5xnhobvqXh9OAKLD5.j5jJrWwCGJfV6oiDS.Il5SYeGKuOYWi','01234567890','1960-03-02','황수미4',2,0,'2020-07-23 13:22:43.513022','2020-07-23 13:22:43.514134'),(5,'logintest5@naver.com','$2b$12$nGccY9cfnDl1y.pRDTM/9uXLNWnKUEO1azzhBI0BZKVm93wjLThyC','01234567890','1950-03-02','황수미5',2,0,'2020-07-24 03:11:53.400620','2020-07-24 03:11:53.402437'),(6,'logintest6@naver.com','$2b$12$ewQKvpcoqJpggh0ltAUmS.hZZseB76fsFYlznpvVUtqLphrCrNAB.','01234567890','1940-03-02','황수미6',2,0,'2020-07-24 08:21:49.586678','2020-07-24 08:21:49.588971'),(7,'logintest7@naver.com','$2b$12$JyT6Wi0rieNqtuKejaVG2.jVD7dhrdx0sx8imZyPXPRtxagMrvsI6','12345678910','1990-03-02','황수미7',1,0,'2020-07-25 06:06:09.845886','2020-07-25 06:06:09.848030'),(8,'logintest8@naver.com','$2b$12$0f82hWAeovgpJkImeyNqsu9O6KVP7O7dqynaNpG7OeKMSPBYrU.UC','12345678910','1990-03-02','황수미8',1,0,'2020-07-25 07:28:00.952724','2020-07-25 07:28:00.957524'),(9,'logintest9@naver.com','$2b$12$5zSZq4FiJ54eX.C05pvtBuuRMybDD4B4YwpEqJH7F1hruCWI7LgbW','12345678910','1990-03-02','황수미9',1,0,'2020-07-26 23:56:25.039797','2020-07-26 23:56:25.054515'),(10,'logintest9@naver.com','$2b$12$QP8iLw/ybPynPc8Kjj21Ae67rsjdLT1xw8U9xfEsrkKoI/w8kUI1e','12345678910','1990-03-02','황수미10',1,0,'2020-07-27 04:33:45.132992','2020-07-27 04:33:45.135295'),(11,'logintest11@naver.com','$2b$12$3ortsp1V8WWeO0xHg5SMwuPVDfpQ.bWBsH6O6zlrP4v6poc3Hp7su','12345678910','1990-03-02','황수미11',1,0,'2020-07-27 04:44:49.396642','2020-07-27 04:44:49.403278'),(12,'test2@test.com','$2b$12$VCoH27G3F.q2J5p44H4HkuNXCdl20eO6Esm/M.T.8c2w0HMHkNTJ6','123-1234-1234','1992-03-02','이윤식',1,0,'2020-07-27 04:51:19.878684','2020-07-27 04:51:19.881225'),(13,'logintest11@naver.com','$2b$12$dGrEiz1d8eB5NYRRQb3p0uTOEMFBBjzs56seGHyTcs38YUObc3q7.','12345678910','1990-03-02','황수미',1,0,'2020-07-30 11:14:45.056776','2020-07-30 11:14:45.061031'),(14,'logintest11@naver.com','$2b$12$b5gzB.jOiuvSXKzBH1X0LObGAnrl5hTuVTXw7yguMehnseDDtG5hW','12345678910','1990-03-02','황수미',1,0,'2020-07-30 11:15:11.368880','2020-07-30 11:15:11.370847'),(15,'logintest13@naver.com','$2b$12$FBAyt5q7m86IK3k4Q1x9Ru2oSGXapbOXylt81d8f6rJEcAs4tV61C','12345678910','1990-03-02','황수미',1,0,'2020-07-30 11:34:04.925240','2020-07-30 11:34:04.927018'),(16,'logintest14@naver.com','$2b$12$LLAm4qB9fa/sWCDS052EVeOUA/oLNIdX9Um.2qsaxLZH/7lvty0Fe','12345678910','1990-03-02','황수미',2,0,'2020-07-30 12:02:44.092279','2020-07-30 12:02:44.093884'),(17,'logintest15@naver.com','$2b$12$0d4Q0/CBx9to/k8jmQBMt.axs8ldzlMmdxCwA/rpXoLeQBkFF1R1y','12345678910','1990-03-02','황수미',2,0,'2020-07-31 04:52:58.394600','2020-07-31 04:52:58.412189');
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

-- Dump completed on 2020-07-31 14:10:01
