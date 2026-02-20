import papermill as pm

def main():
    for configuration in ["A", "B", "C", "D", "M", "N", "O", "P"]: #[chr(i) for i in range(ord('A'), ord('P')+1)]:
        for scenario in [1, 2, 3]:
            for eps_var in [1, 4, 9]:
                print(f"Running experiment {configuration}: {scenario}, noise level={eps_var}")
                try:
                    pm.execute_notebook(
                       "02_experiment_run.ipynb",
                       f"results/{configuration}_{scenario}_{eps_var}.ipynb",
                       parameters=dict(
                           configuration=configuration,
                           scenario=f"{scenario}_{eps_var}"
                       ))
                except Exception as e:
                    print(e)


if __name__ == "__main__":
    main()
