-- creates MySQL database hbnb_test_db only if not existing
-- and gives privileges to user hbnb_test on 2 DB's
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.*
      TO hbnb_test@localhost
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT PRIVILEGES ON performance_schema.*
      TO hbnb_test@localhost
      IDENTIFIED BY 'hbnb_test_pwd';
