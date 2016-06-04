CREATE TABLE `house` (
  `id` varchar(30) NOT NULL DEFAULT '',
  `url` varchar(256) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `price` varchar(10) DEFAULT NULL,
  `room` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `area_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;