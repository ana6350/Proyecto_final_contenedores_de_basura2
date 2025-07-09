--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9
-- Dumped by pg_dump version 16.9

-- Started on 2025-07-09 00:37:48

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 17510)
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- TOC entry 5719 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 17502)
-- Name: contenedor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contenedor (
    fecha date NOT NULL,
    direccion character varying(100) NOT NULL,
    estado character varying(100) NOT NULL,
    observacion character varying(300) NOT NULL,
    foto character varying(100) NOT NULL,
    id integer NOT NULL,
    localizacion public.geometry(Point,4326)
);


ALTER TABLE public.contenedor OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 18593)
-- Name: contenedor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contenedor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contenedor_id_seq OWNER TO postgres;

--
-- TOC entry 5720 (class 0 OID 0)
-- Dependencies: 222
-- Name: contenedor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contenedor_id_seq OWNED BY public.contenedor.id;


--
-- TOC entry 5558 (class 2604 OID 18594)
-- Name: contenedor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contenedor ALTER COLUMN id SET DEFAULT nextval('public.contenedor_id_seq'::regclass);


--
-- TOC entry 5712 (class 0 OID 17502)
-- Dependencies: 216
-- Data for Name: contenedor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contenedor (fecha, direccion, estado, observacion, foto, id, localizacion) FROM stdin;
\.


--
-- TOC entry 5557 (class 0 OID 17828)
-- Dependencies: 218
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- TOC entry 5721 (class 0 OID 0)
-- Dependencies: 222
-- Name: contenedor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contenedor_id_seq', 1, false);


--
-- TOC entry 5561 (class 2606 OID 18601)
-- Name: contenedor contenedor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contenedor
    ADD CONSTRAINT contenedor_pkey PRIMARY KEY (id);


-- Completed on 2025-07-09 00:37:48

--
-- PostgreSQL database dump complete
--

