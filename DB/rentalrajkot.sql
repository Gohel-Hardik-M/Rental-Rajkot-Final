--
-- PostgreSQL database dump
--

\restrict 6T3EdyTsnTmwadS5Un2fFa6DqRIY5oX3zSeP5pl9BF1lmIbZFTL4t6NwecWElcg

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-07-25 13:42:10

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

--
-- TOC entry 862 (class 1247 OID 37164)
-- Name: gender_preference_enum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.gender_preference_enum AS ENUM (
    'BOYS',
    'GIRLS',
    'ANY'
);


ALTER TYPE public.gender_preference_enum OWNER TO postgres;

--
-- TOC entry 859 (class 1247 OID 37159)
-- Name: property_type_enum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.property_type_enum AS ENUM (
    'HOSTEL',
    'ROOM'
);


ALTER TYPE public.property_type_enum OWNER TO postgres;

--
-- TOC entry 223 (class 1255 OID 37157)
-- Name: get_user_by_email(character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.get_user_by_email(p_email character varying) RETURNS TABLE(id integer, full_name character varying, email character varying, phone character varying, password character varying, user_type character varying)
    LANGUAGE plpgsql
    AS $$

BEGIN

    RETURN QUERY

    SELECT
        u.user_id,
        u.full_name,
        u.email,
        u.phone,
        u.password,
        u.user_type

    FROM users u

    WHERE u.email = p_email;

END;

$$;


ALTER FUNCTION public.get_user_by_email(p_email character varying) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 37261)
-- Name: listings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.listings (
    listing_id integer NOT NULL,
    owner_id integer NOT NULL,
    property_type character varying(20) NOT NULL,
    property_name character varying(150) NOT NULL,
    area character varying(100) NOT NULL,
    full_address text NOT NULL,
    nearest_college character varying(150),
    gender_preference character varying(20) NOT NULL,
    description text,
    facilities text[] DEFAULT '{}'::text[],
    monthly_rent numeric(10,2) NOT NULL,
    security_deposit numeric(10,2) NOT NULL,
    other_charges text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.listings OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 37260)
-- Name: listings_listing_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.listings_listing_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.listings_listing_id_seq OWNER TO postgres;

--
-- TOC entry 4991 (class 0 OID 0)
-- Dependencies: 221
-- Name: listings_listing_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.listings_listing_id_seq OWNED BY public.listings.listing_id;


--
-- TOC entry 220 (class 1259 OID 37014)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    full_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    phone character varying(15) NOT NULL,
    password character varying(255) NOT NULL,
    user_type character varying(20) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 37013)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- TOC entry 4992 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 4823 (class 2604 OID 37264)
-- Name: listings listing_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.listings ALTER COLUMN listing_id SET DEFAULT nextval('public.listings_listing_id_seq'::regclass);


--
-- TOC entry 4821 (class 2604 OID 37017)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4985 (class 0 OID 37261)
-- Dependencies: 222
-- Data for Name: listings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.listings (listing_id, owner_id, property_type, property_name, area, full_address, nearest_college, gender_preference, description, facilities, monthly_rent, security_deposit, other_charges, created_at, updated_at) FROM stdin;
2	1	room	1BHK Room 	jamnagar-road	Sarda Colony , KKV Chowk Rajkot	rk-university	Girls Only	1BHK Room With Furniture and Water Supply For Rent in Sarda Colony Rajkot.	{wifi,food,ac,parking,cctv,power_backup,geyser,laundry,kitchen,housekeeping}	8000.00	2000.00	No Other Extra Charges	2026-07-24 11:55:55.196877	2026-07-24 11:55:55.196877
3	1	hostel	Shreeji Premium Boys Hostel	kalavad-road	Bhaktinagar Colony Street No : 5	vvp-engineering-college	Boys Only	Boys Hostel With Premium Rooms and Furnitures.	{wifi,food,ac,parking,cctv,laundry}	12000.00	3000.00	No Charges	2026-07-24 12:41:16.521121	2026-07-24 12:41:16.521121
\.


--
-- TOC entry 4983 (class 0 OID 37014)
-- Dependencies: 220
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, full_name, email, phone, password, user_type, created_at) FROM stdin;
1	Hardikbhai Gohel	hardikbhai.gohel@tssconsultancy.com	1234567890	12345678	OWNER	2026-07-17 13:48:26.351369
7	Raftra	raftra@gmail.com	9909900900	123123	OWNER	2026-07-20 10:48:53.812073
9	ABCD	aa@gmail.com	2290022900	123123	OWNER	2026-07-20 11:18:21.204247
1151	jnb	jnb@gmail.com	9510145725	JnB@21@30#2006	admin	2026-07-24 15:52:30.525693
\.


--
-- TOC entry 4993 (class 0 OID 0)
-- Dependencies: 221
-- Name: listings_listing_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.listings_listing_id_seq', 3, true);


--
-- TOC entry 4994 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 9, true);


--
-- TOC entry 4834 (class 2606 OID 37280)
-- Name: listings listings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.listings
    ADD CONSTRAINT listings_pkey PRIMARY KEY (listing_id);


--
-- TOC entry 4828 (class 2606 OID 37028)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 4830 (class 2606 OID 37030)
-- Name: users users_phone_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_phone_key UNIQUE (phone);


--
-- TOC entry 4832 (class 2606 OID 37026)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


-- Completed on 2026-07-25 13:42:12

--
-- PostgreSQL database dump complete
--

\unrestrict 6T3EdyTsnTmwadS5Un2fFa6DqRIY5oX3zSeP5pl9BF1lmIbZFTL4t6NwecWElcg

