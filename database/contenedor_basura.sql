--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9
-- Dumped by pg_dump version 16.9

-- Started on 2025-07-09 00:03:17

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
-- TOC entry 2 (class 3079 OID 16398)
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- TOC entry 5716 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 17481)
-- Name: basura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.basura (
    id integer NOT NULL,
    fecha date NOT NULL,
    direccion character varying(100) NOT NULL,
    estado character varying(10) NOT NULL,
    observacion character varying(300) NOT NULL,
    foto character varying(100) NOT NULL,
    localizacion public.geometry(Point,4326)
);


ALTER TABLE public.basura OWNER TO postgres;

--
-- TOC entry 5710 (class 0 OID 17481)
-- Dependencies: 221
-- Data for Name: basura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.basura (id, fecha, direccion, estado, observacion, foto, localizacion) FROM stdin;
\.


--
-- TOC entry 5556 (class 0 OID 16716)
-- Dependencies: 217
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- TOC entry 5561 (class 2606 OID 17487)
-- Name: basura basura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.basura
    ADD CONSTRAINT basura_pkey PRIMARY KEY (id);


-- Completed on 2025-07-09 00:03:17

--
-- PostgreSQL database dump complete
--

