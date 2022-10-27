CREATE TABLE "pokemon"(
    "id" int generated always as identity primary key,
    "nome" VARCHAR(255) NOT NULL
);

CREATE TABLE "ataque_rapido"(
    "id" int generated always as identity primary key,
    "ataque" VARCHAR(255) NOT NULL,
    "dano" INTEGER NOT NULL,
    "dano_pos_segundo" DOUBLE PRECISION NOT NULL,
    "energia_por_segundo" DOUBLE PRECISION NOT NULL
);

CREATE TABLE "pokemon_ataque"(
    "id" int generated always as identity primary key,
    "pokemon_id" INTEGER NOT NULL,
    "ataque_rapido_id" INTEGER NOT NULL,
    "ataque_principal_id" INTEGER NOT NULL
);

CREATE TABLE "elemento"(
    "id" int generated always as identity primary key,
    "tipo" VARCHAR(255) NOT NULL
);

CREATE TABLE "pokemon_elemento"(
    "id" int generated always as identity primary key,
    "pokemon_id" INTEGER NOT NULL,
    "tipo_id" INTEGER NOT NULL
);

CREATE TABLE "ataque_principal"(
    "id" int generated always as identity primary key,
    "ataque" VARCHAR(255) NULL,
    "dano" INTEGER NOT NULL,
    "dano_por_segundo" DOUBLE PRECISION NOT NULL,
    "energia_por_segundo" DOUBLE PRECISION NOT NULL
);

ALTER TABLE
    "pokemon_elemento" ADD CONSTRAINT "pokemon_elemento_pokemon_id_foreign" FOREIGN KEY("pokemon_id") REFERENCES "pokemon"("id");
ALTER TABLE
    "pokemon_ataque" ADD CONSTRAINT "pokemon_ataque_pokemon_id_foreign" FOREIGN KEY("pokemon_id") REFERENCES "pokemon"("id");
ALTER TABLE
    "pokemon_ataque" ADD CONSTRAINT "pokemon_ataque_ataque_rapido_id_foreign" FOREIGN KEY("ataque_rapido_id") REFERENCES "ataque_rapido"("id");
ALTER TABLE
    "pokemon_ataque" ADD CONSTRAINT "pokemon_ataque_ataque_principal_id_foreign" FOREIGN KEY("ataque_principal_id") REFERENCES "ataque_principal"("id");
ALTER TABLE
    "pokemon_elemento" ADD CONSTRAINT "pokemon_elemento_tipo_id_foreign" FOREIGN KEY("tipo_id") REFERENCES "elemento"("id");