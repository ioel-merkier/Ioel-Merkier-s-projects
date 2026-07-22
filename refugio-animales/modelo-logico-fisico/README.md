
# MODELO LÓGICO
<img width="1217" height="695" alt="Captura de pantalla 2026-07-22 a la(s) 15 58 18" src="https://github.com/user-attachments/assets/5a428fd1-853c-4312-a152-4694887f15a0" />

# MODELO FISICO
<img width="1280" height="690" alt="Captura de pantalla 2026-07-22 a la(s) 15 59 30" src="https://github.com/user-attachments/assets/c1898ee3-3544-4246-8632-9f7e7ba081b6" />

# DDL

CREATE  TABLE CATEGORIA_ACCION_MEDICA ( 
	id_categoria_accion_medica int      NOT NULL,
	descripcion          varchar(max)      NOT NULL,
	CONSTRAINT pk_CATEGORIA_ACCION_MEDICA PRIMARY KEY  ( id_categoria_accion_medica ) 
 );
GO

CREATE  TABLE PADRINO ( 
	id_padrino           int      NOT NULL,
	dni                  varchar(max)      NOT NULL,
	nombre_y_apellido    varchar(max)      NOT NULL,
	fec_nac              date      NULL,
	telefono             varchar(max)      NOT NULL,
	mail                 varchar(max)      NOT NULL,
	monto_total_donado   int     NOT NULL DEFAULT 0,
	sexo                 varchar(1)      NOT NULL,
	fec_alta             date      NOT NULL,
	fec_baja             date      NULL,
	CONSTRAINT pk_PADRINO PRIMARY KEY  ( id_padrino ) 
 );
GO

CREATE  TABLE RESULTADO_VISITA ( 
	id_resultado         int      NOT NULL,
	descripcion          varchar(max)      NULL,
	CONSTRAINT pk_RESULTADO_VISITA PRIMARY KEY  ( id_resultado ) 
 );
GO

CREATE  TABLE TIPO_DE_ANIMAL ( 
	id_tipo_animal       int      NOT NULL,
	descripcion          varchar(max)      NOT NULL,
	CONSTRAINT pk_TIPO_DE_ANIMAL PRIMARY KEY  ( id_tipo_animal ) 
 );
GO

CREATE  TABLE TIPO_DE_EMPLEADO ( 
	id_tipo_de_empleado  int      NOT NULL,
	descripcion          varchar(max)      NOT NULL,
	es_voluntario        bit      NOT NULL DEFAULT 0,
	rol                  varchar(max)      NOT NULL,
	CONSTRAINT pk_TIPO_DE_EMPLEADO PRIMARY KEY  ( id_tipo_de_empleado ) 
 );
GO

CREATE  TABLE TURNO ( 
	id_turno             int      NOT NULL,
	horarios             varchar(max)      NOT NULL,
	descripcion          varchar(max)      NOT NULL,
	CONSTRAINT pk_TURNO PRIMARY KEY  ( id_turno ) 
 );
GO

CREATE  TABLE VISITANTE ( 
	id_visitante         int      NOT NULL,
	nombre_y_apellido    varchar(max)      NOT NULL,
	telefono             varchar(max)      NOT NULL,
	mail                 varchar(max)      NOT NULL,
	sexo                 varchar(1)      NOT NULL,
	fec_nac              date      NOT NULL,
	domicilio            varchar(max)      NOT NULL,
	CONSTRAINT pk_VISITANTE PRIMARY KEY  ( id_visitante ) 
 );
GO

CREATE  TABLE ACCION_MEDICA ( 
	id_accion            int      NOT NULL,
	descripcion          varchar(max)      NOT NULL,
	id_categoria_accion_medica int      NOT NULL,
	CONSTRAINT pk_ACCION_MEDICA PRIMARY KEY  ( id_accion ) 
 );
GO

CREATE  TABLE EMPLEADO ( 
	id_empleado          int      NOT NULL,
	nombre_y_apellido    varchar(max)      NOT NULL,
	sexo                 varchar(1)      NOT NULL,
	telefono             varchar(max)      NOT NULL,
	fec_nac              date      NOT NULL,
	fec_alta             date      NOT NULL,
	fec_baja             date      NULL,
	id_tipo_de_empleado  int      NOT NULL,
	CONSTRAINT pk_EMPLEADO PRIMARY KEY  ( id_empleado ) 
 );
GO

CREATE  TABLE RAZA ( 
	id_raza              int      NOT NULL,
	descripcion          varchar(max)      NOT NULL,
	id_tipo_animal       int      NOT NULL,
	CONSTRAINT pk_RAZA PRIMARY KEY  ( id_raza ) 
 );
GO

CREATE  TABLE TURNO_POR_EMPLEADO ( 
	id_empleado          int      NOT NULL,
	id_turno             int      NOT NULL,
	fecha_desde	date	NOT NULL,
	fecha_hasta	date	NULL,
	CONSTRAINT pk_TURNO_POR_EMPLEADO PRIMARY KEY  ( id_empleado, id_turno ) 
 );
GO

CREATE  TABLE VISITA ( 
	id_visita            int      NOT NULL,
	fec_y_hora_entrada   smalldatetime      NOT NULL,
	fec_y_hora_salida    smalldatetime      NULL,
	id_visitante         int      NOT NULL,
	id_empleado          int      NOT NULL,
	CONSTRAINT pk_VISITA PRIMARY KEY  ( id_visita ) 
 );
GO

CREATE  TABLE ANIMAL ( 
	id_animal            int      NOT NULL,
	nombre               varchar(max)      NOT NULL,
	fec_nac              date      NULL,
	sexo                 varchar(1)      NOT NULL,
	fec_rescate          date      NULL,
	fec_adopcion         date      NULL,
	fec_fallecimiento    date      NULL,
	descripcion_caracter varchar(max)      NULL,
	cant_donaciones      int      NOT NULL DEFAULT 0,
	cant_visitas         int     NOT NULL DEFAULT 0,
	cant_revisiones_medicas int      NOT NULL DEFAULT 0,
	id_tipo_animal       int      NOT NULL,
	id_raza              int      NOT NULL,
	id_padre             int      NULL,
	CONSTRAINT pk_ANIMAL PRIMARY KEY  ( id_animal ) 
 );
GO

CREATE  TABLE PADRINO_POR_ANIMAL ( 
	id_padrino           int      NOT NULL,
	id_animal            int      NOT NULL,
	fecha_desde	date	NOT NULL,
	fecha_hasta	date	NULL,
	CONSTRAINT pk_id_padrino PRIMARY KEY  ( id_padrino, id_animal ) 
 );
GO

CREATE  TABLE REVISION_MEDICA ( 
	id_visita_medica     int      NOT NULL,
	fec_y_hora           smalldatetime      NOT NULL,
	diagnostico          varchar(max)      NOT NULL,
	id_animal            int      NOT NULL,
	id_empleado          int      NOT NULL,
	CONSTRAINT pk_REVISION_MEDICA PRIMARY KEY  ( id_visita_medica ) 
 );
GO

CREATE  TABLE VISITA_POR_ANIMAL ( 
	observaciones        varchar(max)      NULL,
	id_visita            int      NOT NULL,
	id_animal            int      NOT NULL,
	id_resultado         int      NOT NULL,
	CONSTRAINT pk_VISITA_POR_ANIMAL PRIMARY KEY  ( id_visita, id_animal ) 
 );
GO

CREATE  TABLE ACCION_POR_REVISION ( 
	fec_accion                  smalldatetime      NOT NULL,
	observaciones        varchar(max)      NULL,
	id_accion            int      NOT NULL,
	id_visita_medica     int      NOT NULL,
	CONSTRAINT pk_ACCION_POR_REVISION PRIMARY KEY  ( id_accion, id_visita_medica ) 
 );
GO

CREATE  TABLE DONACION ( 
	id_donacion          int      NOT NULL,
	fec_donacion         date      NOT NULL,
	monto                int      NOT NULL,
	forma_de_pago        varchar(max)      NOT NULL,
	id_padrino           int      NOT NULL,
	id_animal            int      NOT NULL,
	CONSTRAINT pk_DONACION PRIMARY KEY  ( id_donacion ) 
 );
GO

ALTER TABLE ACCION_MEDICA ADD CONSTRAINT fk_ACCION_MEDICA_CATEGORIA_ACCION_MEDICA FOREIGN KEY ( id_categoria_accion_medica ) REFERENCES CATEGORIA_ACCION_MEDICA( id_categoria_accion_medica );
GO

ALTER TABLE ACCION_POR_REVISION ADD CONSTRAINT fk_ACCION_POR_REVISION_ACCION_MEDICA FOREIGN KEY ( id_accion ) REFERENCES ACCION_MEDICA( id_accion );
GO

ALTER TABLE ACCION_POR_REVISION ADD CONSTRAINT fk_ACCION_POR_REVISION_REVISION_MEDICA FOREIGN KEY ( id_visita_medica ) REFERENCES REVISION_MEDICA( id_visita_medica );
GO

ALTER TABLE ANIMAL ADD CONSTRAINT fk_ANIMAL_TIPO_DE_ANIMAL FOREIGN KEY ( id_tipo_animal ) REFERENCES TIPO_DE_ANIMAL( id_tipo_animal );
GO

ALTER TABLE ANIMAL ADD CONSTRAINT fk_ANIMAL_RAZA FOREIGN KEY ( id_raza ) REFERENCES RAZA( id_raza );
GO

ALTER TABLE ANIMAL ADD CONSTRAINT fk_ANIMAL_PADRE FOREIGN KEY ( id_padre ) REFERENCES ANIMAL( id_animal );
GO

ALTER TABLE DONACION ADD CONSTRAINT fk_DONACION_PADRINO_POR_ANIMAL FOREIGN KEY ( id_padrino, id_animal ) REFERENCES PADRINO_POR_ANIMAL( id_padrino, id_animal );
GO

ALTER TABLE EMPLEADO ADD CONSTRAINT fk_EMPLEADO_TIPO_DE_EMPLEADO FOREIGN KEY ( id_tipo_de_empleado ) REFERENCES TIPO_DE_EMPLEADO( id_tipo_de_empleado );
GO

ALTER TABLE PADRINO_POR_ANIMAL ADD CONSTRAINT fk_PADRINO_POR_ANIMAL_PADRINO FOREIGN KEY ( id_padrino ) REFERENCES PADRINO( id_padrino );
GO

ALTER TABLE PADRINO_POR_ANIMAL ADD CONSTRAINT fk_PADRINO_POR_ANIMAL_ANIMAL FOREIGN KEY ( id_animal ) REFERENCES ANIMAL( id_animal );
GO

ALTER TABLE RAZA ADD CONSTRAINT fk_RAZA_TIPO_DE_ANIMAL FOREIGN KEY ( id_tipo_animal ) REFERENCES TIPO_DE_ANIMAL( id_tipo_animal );
GO

ALTER TABLE REVISION_MEDICA ADD CONSTRAINT fk_REVISION_MEDICA_ANIMAL FOREIGN KEY ( id_animal ) REFERENCES ANIMAL( id_animal );
GO

ALTER TABLE REVISION_MEDICA ADD CONSTRAINT fk_REVISION_MEDICA_EMPLEADO FOREIGN KEY ( id_empleado ) REFERENCES EMPLEADO( id_empleado );
GO

ALTER TABLE TURNO_POR_EMPLEADO ADD CONSTRAINT fk_TURNO_POR_EMPLEADO_EMPLEADO FOREIGN KEY ( id_empleado ) REFERENCES EMPLEADO( id_empleado );
GO

ALTER TABLE TURNO_POR_EMPLEADO ADD CONSTRAINT fk_TURNO_POR_EMPLEADO_TURNO FOREIGN KEY ( id_turno ) REFERENCES TURNO( id_turno );
GO

ALTER TABLE VISITA ADD CONSTRAINT fk_VISITA_VISITANTE FOREIGN KEY ( id_visitante ) REFERENCES VISITANTE( id_visitante );
GO

ALTER TABLE VISITA ADD CONSTRAINT fk_VISITA_EMPLEADO FOREIGN KEY ( id_empleado ) REFERENCES EMPLEADO( id_empleado );
GO

ALTER TABLE VISITA_POR_ANIMAL ADD CONSTRAINT fk_VISITA_POR_ANIMAL_VISITA FOREIGN KEY ( id_visita ) REFERENCES VISITA( id_visita );
GO

ALTER TABLE VISITA_POR_ANIMAL ADD CONSTRAINT fk_VISITA_POR_ANIMAL_ANIMAL FOREIGN KEY ( id_animal ) REFERENCES ANIMAL( id_animal );
GO

ALTER TABLE VISITA_POR_ANIMAL ADD CONSTRAINT fk_VISITA_POR_ANIMAL_RESULTADO_VISITA FOREIGN KEY ( id_resultado ) REFERENCES RESULTADO_VISITA( id_resultado );
GO

