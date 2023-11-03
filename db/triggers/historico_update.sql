USE sio-store;
GO

CREATE TRIGGER compra_efetuada
AFTER INSERT ON Compras FOR EACH ROW
BEGIN
    INSERT INTO historico_compras (cliente_id, produto_id, data_compra, quantidade, preco_total)
    VALUES (NEW.cliente_id, NEW.produto_id, NEW.data_compra, NEW.quantidade, NEW.preco_total);
END;
