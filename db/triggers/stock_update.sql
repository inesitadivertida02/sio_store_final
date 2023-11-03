USE sio-store;
GO

CREATE TRIGGER compra_efetuada
AFTER INSERT ON Compras FOR EACH ROW
BEGIN
    DECLARE quantidade_a_remover INT;
    SET quantidade_a_remover = NEW.quantidade;
    
    UPDATE Stock
    SET quantidade = quantidade - quantidade_a_remover
    WHERE produto_id = NEW.produto_id;
END;