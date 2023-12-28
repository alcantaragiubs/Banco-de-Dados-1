-- Checar espaço de inventário 

CREATE OR REPLACE FUNCTION check_inventory_space()
RETURNS TRIGGER AS $$

DECLARE 
  counts INTEGER := 0;

BEGIN
  counts = (SELECT COUNT (Item.id) FROM item WHERE id_inventario = NEW.id_inventario);
  IF (counts >= 3) THEN
    RAISE EXCEPTION 'Inventário Cheio!';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER inventory_full_exception
BEFORE UPDATE OF id_inventario ON Item
FOR EACH ROW EXECUTE FUNCTION check_inventory_space();

--- Retornar count de itens no inventário

CREATE OR REPLACE FUNCTION count_items() RETURNS integer AS $$  
     BEGIN
     RETURN (SELECT COUNT (Item.id) FROM item WHERE id_inventario = NEW.id_inventario);
    END $$ LANGUAGE plpgsql;


-- Impedir duplicados na tabela Nível

CREATE OR REPLACE FUNCTION prevent_duplicate_nivel()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT * FROM Nivel WHERE descricao = NEW.descricao) THEN
    RAISE EXCEPTION 'Esse Nível, já existe!';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_nivel_insert
BEFORE INSERT ON Nivel
FOR EACH ROW EXECUTE FUNCTION prevent_duplicate_nivel();

-- Impedir duplicados na tabela Item

CREATE OR REPLACE FUNCTION prevent_duplicate_item()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT * FROM Item WHERE nome = NEW.nome AND descricao = NEW.descricao) THEN
    RAISE EXCEPTION 'Esse Item já existe!';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_item_insert
BEFORE INSERT ON Item
FOR EACH ROW EXECUTE FUNCTION prevent_duplicate_item();

-- Impedir duplicados na tabela Sala

CREATE OR REPLACE FUNCTION prevent_duplicate_sala()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT * FROM Sala WHERE nome = NEW.nome AND descricao = NEW.descricao) THEN
    RAISE EXCEPTION 'Essa sala já existe!';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_sala_insert
BEFORE INSERT ON Sala
FOR EACH ROW EXECUTE FUNCTION prevent_duplicate_sala();

-- Impedir duplicados na tabela Jogador

CREATE OR REPLACE FUNCTION prevent_duplicate_jogador()
RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT * FROM Jogador WHERE nome = NEW.nome) THEN
    RAISE EXCEPTION 'Esse Usuário já existe';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;



CREATE TRIGGER prevent_duplicate_jogador_insert
BEFORE INSERT ON Jogador
FOR EACH ROW EXECUTE FUNCTION prevent_duplicate_jogador();

-- Impedir duplicados na tabela Inventário

CREATE OR REPLACE FUNCTION prevent_duplicates_in_inventario()
RETURNS TRIGGER AS $$
BEGIN
IF EXISTS (SELECT id FROM Inventario WHERE id_jogador = NEW.id_jogador) THEN
RAISE EXCEPTION 'Esse jogador já tem um inventário!';
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_inventario_insert
BEFORE INSERT ON Inventario
FOR EACH ROW EXECUTE FUNCTION prevent_duplicates_in_inventario();

-- Cria Inventario quando é criado um jogador

CREATE OR REPLACE FUNCTION creates_inventario_when_create_jogador()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO Inventario (tamanho_inventario, id_jogador)
  VALUES (3, NEW.id);
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER create_inventario
AFTER INSERT ON Jogador
FOR EACH ROW
EXECUTE FUNCTION creates_inventario_when_create_jogador();


--- Impedir duplicados na tabela NPC

CREATE OR REPLACE FUNCTION prevent_duplicates_in_NPC()
RETURNS TRIGGER AS $$
BEGIN
IF EXISTS (SELECT id FROM NPC WHERE nome = NEW.nome AND id_sala = NEW.id_sala) THEN
RAISE EXCEPTION 'O NPC já existe nessa sala!';
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_NPC_insert
BEFORE INSERT ON NPC
FOR EACH ROW EXECUTE FUNCTION prevent_duplicates_in_NPC();


--- Impedir duplicados na tabela Boss

CREATE OR REPLACE FUNCTION prevent_duplicates_in_boss()
RETURNS TRIGGER AS $$
BEGIN
IF EXISTS (SELECT id FROM Boss WHERE nome = NEW.nome AND id_nivel = NEW.id_nivel) THEN
RAISE EXCEPTION 'Esse Boss já está presente no nível!';
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_boss_insert
BEFORE INSERT ON Boss
FOR EACH ROW EXECUTE FUNCTION prevent_duplicates_in_boss();


--- Impedir duplicados na tabela Codigo

CREATE OR REPLACE FUNCTION prevent_duplicates_in_codigo()
RETURNS TRIGGER AS $$
BEGIN
IF EXISTS (SELECT id FROM Codigo WHERE nome = NEW.nome AND descricao = NEW.descricao) THEN
RAISE EXCEPTION 'Código Duplicado!';
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER prevent_duplicate_codigo_insert
BEFORE INSERT ON Codigo
FOR EACH ROW EXECUTE FUNCTION prevent_duplicates_in_codigo();

