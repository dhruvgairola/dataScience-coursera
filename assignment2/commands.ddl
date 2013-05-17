-- (q1)
-- select count(*) from Frequency where docid = '10398_txt_earn';
-- (q2)
-- select count(*) from Frequency where docid = '10398_txt_earn' and count = 1;
-- (q3)
-- select count(term) from (select distinct term from Frequency where (docid = '10398_txt_earn' or docid = '925_txt_trade') and count = 1);
-- (q4)
-- select count(docid) from Frequency where term = 'parliament';
-- (q5)
-- select count(sum_count) from (select sum(count) as sum_count from Frequency group by docid) where sum_count > 300;
-- (q6)
-- select count(distinct docid) from Frequency where docid in (select docid from Frequency where term='transactions') and term='world';

-- (q7) : Read coursera doc on evernote in order to understand the query below
-- select output from (select sum(A.value * B.value) as output, A.row_num as arow, B.col_num as bcol from A join B where (A.col_num=B.row_num) group by A.row_num, B.col_num) where arow = 2 and bcol = 3;

-- (q8) : Read coursera doc on evernote in order to understand the query below
-- select sum(c1 * c2) from (select term as t1, count as c1 from Frequency where docid = '10080_txt_crude') join (select term as t2, count as c2 from Frequency where docid = '17035_txt_earn') where t1=t2;

-- (q9)
-- create view search as SELECT * FROM frequency UNION SELECT 'q' as docid, 'washington' as term, 1 as count UNION SELECT 'q' as docid, 'taxes' as term, 1 as count UNION SELECT 'q' as docid, 'treasury' as term, 1 as count;
-- select d2, sum(c1 * c2) as keyword_sim from (select docid as d1, term as t1, count as c1 from search where docid = 'q') join (select docid as d2, term as t2, count as c2 from search) where t1 = t2 group by d2 order by keyword_sim desc limit 1;