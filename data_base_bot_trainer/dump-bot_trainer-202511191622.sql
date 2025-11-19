--
-- PostgreSQL database dump
--

\restrict J9ah1d3wAEab6iZXRKdHxqE06Ga0GldSnJxWibhYKiLhVCVs0VjhjfwY3Ymlz3z

-- Dumped from database version 17.7
-- Dumped by pg_dump version 17.7

-- Started on 2025-11-19 16:22:33

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
-- TOC entry 223 (class 1259 OID 16451)
-- Name: booking; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.booking (
    id_booking integer NOT NULL,
    client_id bigint NOT NULL,
    slot_id integer NOT NULL,
    status character varying(20) DEFAULT 'active'::character varying,
    created_at timestamp without time zone DEFAULT now(),
    client_name character varying(255),
    client_phone character varying(50),
    trainer_id integer
);


ALTER TABLE public.booking OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16450)
-- Name: booking_id_booking_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.booking_id_booking_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.booking_id_booking_seq OWNER TO postgres;

--
-- TOC entry 4833 (class 0 OID 0)
-- Dependencies: 222
-- Name: booking_id_booking_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.booking_id_booking_seq OWNED BY public.booking.id_booking;


--
-- TOC entry 217 (class 1259 OID 16422)
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    id_client bigint NOT NULL,
    full_name character varying(255) NOT NULL,
    phone character varying(50),
    username character varying(100),
    created_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.client OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16438)
-- Name: schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schedule (
    id_slot integer NOT NULL,
    trainer_id integer NOT NULL,
    slot_timestamp timestamp without time zone NOT NULL,
    status character varying(20) DEFAULT 'free'::character varying
);


ALTER TABLE public.schedule OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16437)
-- Name: schedule_id_slot_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.schedule_id_slot_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.schedule_id_slot_seq OWNER TO postgres;

--
-- TOC entry 4834 (class 0 OID 0)
-- Dependencies: 220
-- Name: schedule_id_slot_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.schedule_id_slot_seq OWNED BY public.schedule.id_slot;


--
-- TOC entry 219 (class 1259 OID 16429)
-- Name: trainer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trainer (
    id_trainer integer NOT NULL,
    full_name character varying(255) NOT NULL,
    qualification text,
    specialization character varying(255),
    contacts text,
    about text
);


ALTER TABLE public.trainer OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16428)
-- Name: trainer_id_trainer_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.trainer_id_trainer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.trainer_id_trainer_seq OWNER TO postgres;

--
-- TOC entry 4835 (class 0 OID 0)
-- Dependencies: 218
-- Name: trainer_id_trainer_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.trainer_id_trainer_seq OWNED BY public.trainer.id_trainer;


--
-- TOC entry 4659 (class 2604 OID 16454)
-- Name: booking id_booking; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking ALTER COLUMN id_booking SET DEFAULT nextval('public.booking_id_booking_seq'::regclass);


--
-- TOC entry 4657 (class 2604 OID 16441)
-- Name: schedule id_slot; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule ALTER COLUMN id_slot SET DEFAULT nextval('public.schedule_id_slot_seq'::regclass);


--
-- TOC entry 4656 (class 2604 OID 16432)
-- Name: trainer id_trainer; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainer ALTER COLUMN id_trainer SET DEFAULT nextval('public.trainer_id_trainer_seq'::regclass);


--
-- TOC entry 4827 (class 0 OID 16451)
-- Dependencies: 223
-- Data for Name: booking; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.booking (id_booking, client_id, slot_id, status, created_at, client_name, client_phone, trainer_id) FROM stdin;
1	123456	1	active	2025-11-19 15:34:39.922398	Иван Иванов	+79991234567	\N
2	234567	3	active	2025-11-19 15:34:39.927381	Мария Петрова	+79997654321	\N
\.


--
-- TOC entry 4821 (class 0 OID 16422)
-- Dependencies: 217
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client (id_client, full_name, phone, username, created_at) FROM stdin;
123456	Иван Иванов	+79991234567	ivan	2025-11-19 15:34:39.705658
234567	Мария Петрова	+79997654321	maria	2025-11-19 15:34:39.705658
\.


--
-- TOC entry 4825 (class 0 OID 16438)
-- Dependencies: 221
-- Data for Name: schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schedule (id_slot, trainer_id, slot_timestamp, status) FROM stdin;
1	1	2025-11-20 15:34:39.903444	free
2	1	2025-11-21 15:34:39.903444	free
3	2	2025-11-20 15:34:39.903444	free
4	2	2025-11-22 15:34:39.903444	free
\.


--
-- TOC entry 4823 (class 0 OID 16429)
-- Dependencies: 219
-- Data for Name: trainer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trainer (id_trainer, full_name, qualification, specialization, contacts, about) FROM stdin;
1	Алексей Смирнов	Сертификат тренера	Йога	\N	\N
2	Екатерина Кузнецова	Сертификат фитнес	Пилатес	\N	\N
\.


--
-- TOC entry 4836 (class 0 OID 0)
-- Dependencies: 222
-- Name: booking_id_booking_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.booking_id_booking_seq', 2, true);


--
-- TOC entry 4837 (class 0 OID 0)
-- Dependencies: 220
-- Name: schedule_id_slot_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.schedule_id_slot_seq', 4, true);


--
-- TOC entry 4838 (class 0 OID 0)
-- Dependencies: 218
-- Name: trainer_id_trainer_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.trainer_id_trainer_seq', 2, true);


--
-- TOC entry 4669 (class 2606 OID 16458)
-- Name: booking booking_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_pkey PRIMARY KEY (id_booking);


--
-- TOC entry 4663 (class 2606 OID 16427)
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id_client);


--
-- TOC entry 4667 (class 2606 OID 16444)
-- Name: schedule schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT schedule_pkey PRIMARY KEY (id_slot);


--
-- TOC entry 4665 (class 2606 OID 16436)
-- Name: trainer trainer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainer
    ADD CONSTRAINT trainer_pkey PRIMARY KEY (id_trainer);


--
-- TOC entry 4671 (class 2606 OID 16460)
-- Name: booking unique_slot_booking; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT unique_slot_booking UNIQUE (slot_id);


--
-- TOC entry 4673 (class 2606 OID 16461)
-- Name: booking fk_booking_client; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT fk_booking_client FOREIGN KEY (client_id) REFERENCES public.client(id_client) ON DELETE CASCADE;


--
-- TOC entry 4674 (class 2606 OID 16466)
-- Name: booking fk_booking_slot; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT fk_booking_slot FOREIGN KEY (slot_id) REFERENCES public.schedule(id_slot) ON DELETE CASCADE;


--
-- TOC entry 4675 (class 2606 OID 16471)
-- Name: booking fk_booking_trainer; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT fk_booking_trainer FOREIGN KEY (trainer_id) REFERENCES public.trainer(id_trainer) ON DELETE CASCADE;


--
-- TOC entry 4672 (class 2606 OID 16445)
-- Name: schedule fk_schedule_trainer; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT fk_schedule_trainer FOREIGN KEY (trainer_id) REFERENCES public.trainer(id_trainer) ON DELETE CASCADE;


-- Completed on 2025-11-19 16:22:33

--
-- PostgreSQL database dump complete
--

\unrestrict J9ah1d3wAEab6iZXRKdHxqE06Ga0GldSnJxWibhYKiLhVCVs0VjhjfwY3Ymlz3z

