USE sio-store;
GO

CREATE TRIGGER verificar_estoque
BEFORE INSERT ON Compras
FOR EACH ROW
BEGIN
    DECLARE estoque_disponivel INT;
    SELECT quantidade INTO estoque_disponivel
    FROM Stock
    WHERE produto_id = NEW.produto_id;
    
    IF estoque_disponivel < NEW.quantidade THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Estoque insuficiente para este produto.';
    END IF;
END;

