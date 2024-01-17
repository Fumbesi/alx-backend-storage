-- 4-store.sql
-- Script to create a trigger to update item quantity after adding a new order

-- Create the trigger
DELIMITER //
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
