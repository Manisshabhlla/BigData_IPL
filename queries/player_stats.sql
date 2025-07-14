SELECT
  batsman,
  season,
  SUM(batsman_runs) AS total_runs,
  COUNT(DISTINCT match_id) AS matches,
  ROUND(SUM(batsman_runs)*1.0 / COUNT(DISTINCT match_id), 2) AS avg_runs
FROM `your-gcp-project.ipl_dataset.ipl_matches`
GROUP BY batsman, season
ORDER BY total_runs DESC
LIMIT 10;
