from sqlalchemy import create_engine
engine = create_engine('postgresql://wg_forge:42a@localhost:5432/wg_forge_db')
db = engine.connect()

# Exercise 1
def first():
    db.execute("""INSERT into cat_colors_info(color,count)
               SELECT color, COUNT(*)
               FROM cats
               GROUP BY color""")
# Exercise 2
def second():
    db.execute("""INSERT INTO cats_stat(tail_length_mean, tail_length_median, tail_length_mode,
                  whiskers_length_mean, whiskers_length_median, whiskers_length_mode)
                  SELECT round(avg(tail_length), 1), PERCENTILE_CONT(0.5)
                  WITHIN GROUP (ORDER BY tail_length), ARRAY[mode()
                  WITHIN GROUP (ORDER BY tail_length DESC)], round(avg(whiskers_length), 1), PERCENTILE_CONT(0.5)
                  WITHIN GROUP (ORDER BY whiskers_length), ARRAY[mode()
                  WITHIN GROUP (ORDER BY whiskers_length ASC), mode()
                  WITHIN GROUP (ORDER BY whiskers_length DESC)] FROM cats""")


first()
second()
print("Success!\n")

