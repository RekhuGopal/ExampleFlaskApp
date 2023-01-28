CREATE DATABASE IF NOT EXISTS `cloudquicklabs` DEFAULT CHARACTER SET  utf8 COLLATE utf8_general_ci;
USE `cloudquicklabs`

CREATE TABLE IF NOT EXISTS `hospitalaccounts`(
    `hospitalid` int(11) NOT NULL AUTO_INCREMENT,
    `password` varchar(255) NOT NULL,
    `email` varchar(100) NOT NULL,
    `hospitalname` varchar(100) NOT NULL,
    `address` varchar(100) NOT NULL,
    `city` varchar(100) NOT NULL,
    `state` varchar(100) NOT NULL,
    `country` varchar(100) NOT NULL,
    `postalcode` varchar(100) NOT NULL,
    `ownername` varchar(100) NOT NULL,
    `phonenumber` varchar(100) NOT NULL,
    `dateofsubscription` DATE,
    `pan` varchar(100) NOT NULL,
    `adhaarcard` varchar(100) NOT NULL,
    `gstin` varchar(100) NOT NULL,
    PRIMARY KEY (`hospitalid`)
) ENGINE=InnoDB AUTO_INCREMENT=133134 DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `hospitalstaff`(
    `hospitalid` int(11),
    `staffid` int(11) NOT NULL AUTO_INCREMENT,
    `password` varchar(255) NOT NULL,
    `email` varchar(100) NOT NULL,
    `staffname` varchar(100) NOT NULL,
    `role` varchar(100) NOT NULL,
    `specialities` varchar(100) NOT NULL,
    `address` varchar(100) NOT NULL,
    `city` varchar(100) NOT NULL,
    `state` varchar(100) NOT NULL,
    `country` varchar(100) NOT NULL,
    `postalcode` varchar(100) NOT NULL,
    `phonenumber` varchar(100) NOT NULL,
    `dateofbirth` DATE,
    `sex` varchar(100) NOT NULL,
    `adhaarcard` varchar(100) NOT NULL,
    PRIMARY KEY (`staffid`)
    FOREIGN KEY (hospitalid) REFERENCES hospitalaccounts(hospitalid)
) ENGINE=InnoDB AUTO_INCREMENT=100000 DEFAULT CHARSET=utf8;