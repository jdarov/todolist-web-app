--
-- PostgreSQL database dump
--

\restrict p80dAZUdsOZ2JsT1kmtWfeFhqdkTR85aBAqOaxt3gfwBgpvdHKjhqQELHqB2saf

-- Dumped from database version 16.10 (Ubuntu 16.10-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.10 (Ubuntu 16.10-0ubuntu0.24.04.1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: lists; Type: TABLE; Schema: public; Owner: jdarov
--

CREATE TABLE public.lists (
    id integer NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.lists OWNER TO jdarov;

--
-- Name: list_id_seq; Type: SEQUENCE; Schema: public; Owner: jdarov
--

CREATE SEQUENCE public.list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.list_id_seq OWNER TO jdarov;

--
-- Name: list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jdarov
--

ALTER SEQUENCE public.list_id_seq OWNED BY public.lists.id;


--
-- Name: todos; Type: TABLE; Schema: public; Owner: jdarov
--

CREATE TABLE public.todos (
    id integer NOT NULL,
    title text NOT NULL,
    completed boolean DEFAULT false,
    list_id integer NOT NULL
);


ALTER TABLE public.todos OWNER TO jdarov;

--
-- Name: todo_id_seq; Type: SEQUENCE; Schema: public; Owner: jdarov
--

CREATE SEQUENCE public.todo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.todo_id_seq OWNER TO jdarov;

--
-- Name: todo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jdarov
--

ALTER SEQUENCE public.todo_id_seq OWNED BY public.todos.id;


--
-- Name: lists id; Type: DEFAULT; Schema: public; Owner: jdarov
--

ALTER TABLE ONLY public.lists ALTER COLUMN id SET DEFAULT nextval('public.list_id_seq'::regclass);


--
-- Name: todos id; Type: DEFAULT; Schema: public; Owner: jdarov
--

ALTER TABLE ONLY public.todos ALTER COLUMN id SET DEFAULT nextval('public.todo_id_seq'::regclass);


--
-- Data for Name: lists; Type: TABLE DATA; Schema: public; Owner: jdarov
--

COPY public.lists (id, title) FROM stdin;
\.


--
-- Data for Name: todos; Type: TABLE DATA; Schema: public; Owner: jdarov
--

COPY public.todos (id, title, completed, list_id) FROM stdin;
\.


--
-- Name: list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jdarov
--

SELECT pg_catalog.setval('public.list_id_seq', 1, false);


--
-- Name: todo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jdarov
--

SELECT pg_catalog.setval('public.todo_id_seq', 1, false);


--
-- Name: lists list_pkey; Type: CONSTRAINT; Schema: public; Owner: jdarov
--

ALTER TABLE ONLY public.lists
    ADD CONSTRAINT list_pkey PRIMARY KEY (id);


--
-- Name: lists list_title_key; Type: CONSTRAINT; Schema: public; Owner: jdarov
--

ALTER TABLE ONLY public.lists
    ADD CONSTRAINT list_title_key UNIQUE (title);


--
-- Name: todos todo_pkey; Type: CONSTRAINT; Schema: public; Owner: jdarov
--

ALTER TABLE ONLY public.todos
    ADD CONSTRAINT todo_pkey PRIMARY KEY (id);


--
-- Name: todos todos_list_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jdarov
--

ALTER TABLE ONLY public.todos
    ADD CONSTRAINT todos_list_id_fkey FOREIGN KEY (list_id) REFERENCES public.lists(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict p80dAZUdsOZ2JsT1kmtWfeFhqdkTR85aBAqOaxt3gfwBgpvdHKjhqQELHqB2saf

