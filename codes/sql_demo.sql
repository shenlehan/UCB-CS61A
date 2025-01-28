create table parents as
    select "abraham" as parent, "barack" as child union
    select "abraham"          , "clinton"         union
    select "delano"           , "herbert"         union
    select "fillmore"         , "abaraham"        union
    select "fillmore"         , "delano"          union
    select "fillmore"         , "grover"          union
    select "eisenhower"       , "fillmore";

