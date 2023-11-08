use kesh;
CREATE TABLE my_table (
     `url` VARCHAR(255),
     `region` VARCHAR(255),
     `region_url` VARCHAR(255),
     `price` INT,
     `year` INT,
     `manufacturer` VARCHAR(255),
     `condition` VARCHAR(255),
     `type` VARCHAR(255),
     `paint_color` VARCHAR(255),
     `image_url` VARCHAR(255)
);
ALTER TABLE my_table MODIFY COLUMN year VARCHAR(255);
ALTER TABLE my_table MODIFY COLUMN price VARCHAR(255);

SHOW VARIABLES LIKE "secure_file_priv";
use kesh;
create table our_table(
    id INT,
    url VARCHAR(255),
    region VARCHAR(255),
    region_url VARCHAR(255),
    price INT,
    year INT,
    manufacturer VARCHAR(255),
    model VARCHAR(255),
    `condition` VARCHAR(255),
    type VARCHAR(255),
    paint_color VARCHAR(255),
    image_url VARCHAR(255),
    description TEXT,
    county VARCHAR(255),
    state VARCHAR(255),
    lat FLOAT,
    `long` FLOAT,
    posting_date DATETIME,
    removal_date DATETIME
);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data.dump.csv'
INTO TABLE our_table
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;



