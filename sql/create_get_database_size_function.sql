-- DROP FUNCTION public.get_database_size();

CREATE OR REPLACE FUNCTION public.get_database_size()
 RETURNS text
 LANGUAGE plpgsql
AS $function$
BEGIN
    RETURN pg_size_pretty(pg_database_size(current_database()));
END;
$function$
;