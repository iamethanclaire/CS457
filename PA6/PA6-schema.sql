--
-- PostgreSQL database dump
--

\restrict 6R35XKbYV2mVLfnjTUbVglojpS3qmKsRjNmxS0gyk9e8PtF9ev9VxOZDPadYCX3

-- Dumped from database version 18.3 (Postgres.app)
-- Dumped by pg_dump version 18.3 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: laptop; Type: TABLE; Schema: public; Owner: ethanclaire
--

CREATE TABLE public.laptop (
    model integer,
    speed numeric(3,2),
    ram integer,
    hd integer,
    screen numeric(3,1),
    price integer,
    maker character varying(1)
);


ALTER TABLE public.laptop OWNER TO ethanclaire;

--
-- Name: maker; Type: TABLE; Schema: public; Owner: ethanclaire
--

CREATE TABLE public.maker (
    name character varying(255),
    founded integer,
    country character varying(255)
);


ALTER TABLE public.maker OWNER TO ethanclaire;

--
-- Name: pc; Type: TABLE; Schema: public; Owner: ethanclaire
--

CREATE TABLE public.pc (
    model integer,
    speed numeric(3,2),
    ram integer,
    hd integer,
    price integer,
    maker character varying(1)
);


ALTER TABLE public.pc OWNER TO ethanclaire;

--
-- Name: printer; Type: TABLE; Schema: public; Owner: ethanclaire
--

CREATE TABLE public.printer (
    model integer,
    color boolean,
    type character varying(255),
    price integer,
    maker character varying(1)
);


ALTER TABLE public.printer OWNER TO ethanclaire;

--
-- PostgreSQL database dump complete
--

\unrestrict 6R35XKbYV2mVLfnjTUbVglojpS3qmKsRjNmxS0gyk9e8PtF9ev9VxOZDPadYCX3

