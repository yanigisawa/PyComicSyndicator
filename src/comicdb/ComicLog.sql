CREATE TABLE `comicdb`.`ComicLog` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ComicId` INT NOT NULL,
  `FetchDate` DATETIME NOT NULL,
  `ImageUrl` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX IX_ComicLog_FetchDate(`FetchDate`),
  CONSTRAINT `FK_Comic_ComicId` FOREIGN KEY `FK_Comic_ComicId` (`ComicId`)
    REFERENCES `Comic` (`Id`)
)
ENGINE = InnoDB
CHARACTER SET utf8;
