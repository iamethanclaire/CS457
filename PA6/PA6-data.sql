--
-- PostgreSQL database dump
--

\restrict VeOl9pKYdVXzKYDv0Svy8mZbhhl4J7kZRdaVpRkw3YB5NgFjsiKCIbnR7axcx5X

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

--
-- Data for Name: laptop; Type: TABLE DATA; Schema: public; Owner: ethanclaire
--

COPY public.laptop (model, speed, ram, hd, screen, price, maker) FROM stdin;
2001	2.00	2048	240	20.1	3673	E
2002	1.73	1024	80	17.0	949	E
2003	1.80	512	60	15.4	549	E
2004	2.00	512	60	13.3	1150	A
2005	2.16	1024	120	17.0	2500	A
2006	2.00	2048	80	15.4	1700	A
2007	1.83	1024	120	13.3	1429	B
2008	1.60	1024	100	15.4	900	F
2009	1.60	512	80	14.1	680	F
2010	2.00	2048	160	15.4	2300	G
\.


--
-- Data for Name: maker; Type: TABLE DATA; Schema: public; Owner: ethanclaire
--

COPY public.maker (name, founded, country) FROM stdin;
A	1989	Taiwan
B	1885	USA
C	1983	Taiwan
D	1984	USA
E	1989	Canada
F	1935	Japan
G	1958	South Korea
H	1939	USA
\.


--
-- Data for Name: pc; Type: TABLE DATA; Schema: public; Owner: ethanclaire
--

COPY public.pc (model, speed, ram, hd, price, maker) FROM stdin;
1001	2.66	1024	250	2114	A
1002	2.10	512	250	995	A
1003	1.42	512	80	478	A
1005	3.20	512	250	630	B
1006	3.20	1024	320	1049	B
1007	2.20	1024	200	510	C
1008	2.20	2048	250	770	D
1009	2.00	1024	250	650	D
1010	2.80	2048	300	770	D
1011	1.86	2048	160	959	E
1012	2.80	1024	160	649	E
1013	3.06	512	80	529	E
1004	2.80	1024	250	649	B
\.


--
-- Data for Name: printer; Type: TABLE DATA; Schema: public; Owner: ethanclaire
--

COPY public.printer (model, color, type, price, maker) FROM stdin;
3001	t	ink-jet	99	E
3002	f	laser	239	E
3003	t	laser	899	E
3004	t	ink-jet	120	D
3005	f	laser	120	D
3006	t	ink-jet	100	H
3007	t	laser	200	H
\.


--
-- PostgreSQL database dump complete
--

\unrestrict VeOl9pKYdVXzKYDv0Svy8mZbhhl4J7kZRdaVpRkw3YB5NgFjsiKCIbnR7axcx5X

