-- User stories:
-- As a shop manager
-- So I can know which items I have in stock
-- I want to keep a list of my shop items with their name and unit price.

-- As a shop manager
-- So I can know which items I have in stock
-- I want to know which quantity (a number) I have for each item.

-- As a shop manager
-- So I can manage items
-- I want to be able to create a new item.

-- As a shop manager
-- So I can know which orders were made
-- I want to keep a list of orders with their customer name.

-- As a shop manager
-- So I can know which orders were made
-- I want to assign each order to their corresponding item.

-- As a shop manager
-- So I can know which orders were made
-- I want to know on which date an order was placed. 

-- As a shop manager
-- So I can manage orders
-- I want to be able to create a new order.

-- Nouns: item name, item price, item quantity, order customer name, order date
-- Actions: create item, assign order to item, create new order

-- items [name, price, quantity]
-- orders[customer_name, date]
-- items_orders [order_id, item_id] -- connecting table

-- Table 1
DROP TABLE items CASCADE;
DROP TABLE IF EXISTS items;
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  price int,
  quantity int
);
INSERT INTO items (name, price, quantity) VALUES ('t-shirt', 10, 30);
INSERT INTO items (name, price, quantity) VALUES ('dress', 30, 40);
INSERT INTO items (name, price, quantity) VALUES ('coat', 100, 20);

-- Table 2
DROP TABLE orders CASCADE;
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  date date
);
INSERT INTO orders (customer_name, date) VALUES ('Amina', '2011-11-11');
INSERT INTO orders (customer_name, date) VALUES ('Jack', '2022-02-22');

-- Table 3 (connecting table)
DROP TABLE items_orders CASCADE;
DROP TABLE IF EXISTS items_orders;
CREATE TABLE items_orders (
  item_id int,
  order_id int,
  constraint fk_item_id foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order_id foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

INSERT INTO items_orders (order_id, item_id) VALUES (1, 1); --Amina everything
INSERT INTO items_orders (order_id, item_id) VALUES (1, 2);
INSERT INTO items_orders (order_id, item_id) VALUES (1, 3);
INSERT INTO items_orders (order_id, item_id) VALUES (2, 1); --Jack just tshirt

-- Write file into database in terminal
-- psql -h 127.0.0.1 database_name < table_name.sql