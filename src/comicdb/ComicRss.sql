CREATE TABLE `comicdb`.`ComicRss` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ComicLogId` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_ComicRss_ComicLog` FOREIGN KEY `FK_ComicRss_ComicLog` (`ComicLogId`)
    REFERENCES `ComicLog` (`id`)
)
ENGINE = InnoDB
CHARACTER SET utf8;
