CREATE TABLE `comicdb`.`Comic` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Name` Varchar(50) NOT NULL,
  `Url` varchar(1000) NOT NULL,
  `ParserConstructor` varchar(200) NOT NULL,
  `IsActive` BOOLEAN NOT NULL,
  PRIMARY KEY (`Id`)
)
ENGINE = InnoDB
CHARACTER SET utf8;
