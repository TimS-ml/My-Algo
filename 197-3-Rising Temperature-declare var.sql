-- https://leetcode-cn.com/problems/rising-temperature/

select Id from (
    select case
        when Temperature > @prevtemp and DATEDIFF(RecordDate, @prevdate) = 1 then Id else null end as Id,
        @prevtemp:=Temperature,
        @prevdate:=RecordDate
    from Weather, (select @prevtemp:=null) as A, (select @prevdate:=null) as B order by RecordDate asc
) as D where Id is not null
