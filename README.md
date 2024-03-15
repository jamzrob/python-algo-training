Katas

## Project Structure Reform
Python version of [Primeagen Typescript course on algorithms](Phttps://github.com/ThePrimeagen/kata-machine)

- [Install poetry](Ihttps://python-poetry.org/docs/)
- Generate a day
```bash
poetry run python scripts/generate.py
```
- Solve the algo
- Test your solution
```bash
poetry run pytest
```
-- Enjoy

## Note
Here is a script to update the tests for a new day
```bash
find . -name "*test*.py" -exec sed -i '' "s/day1/day2/g" {} + 

```
