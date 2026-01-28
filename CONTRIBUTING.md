# Contributing to TravelPy

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Types of Contributions

### Report Bugs

Report bugs by opening a [GitHub issue](https://github.com/UBC-MDS/DSCI_524_group_25/issues).

Please include:
- Your operating system name and version
- Python version
- Detailed steps to reproduce the bug
- Any error messages or tracebacks

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" is open to whoever wants to implement it.

### Write Documentation

TravelPy can always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts and articles.

## Developer Installation

To set up TravelPy for local development:

### Option 1: Using Conda (Recommended)

```bash
# Clone the repository
git clone https://github.com/UBC-MDS/DSCI_524_group_25.git
cd DSCI_524_group_25

# Create and activate conda environment
conda env create -f environment.yml
conda activate travelpy

# Install package in development mode
pip install -e .
```

### Option 2: Using pip and venv

```bash
# Clone the repository
git clone https://github.com/UBC-MDS/DSCI_524_group_25.git
cd DSCI_524_group_25

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package with development dependencies
pip install -e ".[dev,tests,docs]"
```

### Option 3: Using Hatch

```bash
# Clone the repository
git clone https://github.com/UBC-MDS/DSCI_524_group_25.git
cd DSCI_524_group_25

# Enter the default Hatch environment
hatch shell
```

## Running Tests

```bash
# Using pytest directly
pytest --cov=travelpy --cov-report=term-missing

# Using Hatch
hatch run test:run
```

## Code Style

We use [Ruff](https://github.com/astral-sh/ruff) for linting and style checking.

```bash
# Check code style
ruff check src/

# Auto-fix issues
ruff check src/ --fix
```

## Building Documentation

```bash
# Build docs
quartodoc build
quarto render

# Or using Hatch
hatch run docs:build

# Preview docs locally
hatch run docs:serve
```

## Pull Request Guidelines

### Workflow

1. Fork the repository (external contributors) or create a branch (team members)
2. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit with meaningful messages:
   ```bash
   git commit -m "feat: add new feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request against `main`

### Before Submitting

Please ensure your PR:

- [ ] Includes tests for new functionality
- [ ] All tests pass (`hatch run test:run`)
- [ ] Code passes style checks (`ruff check src/`)
- [ ] Documentation is updated if needed
- [ ] Includes an entry in `CHANGELOG.md`
- [ ] Has a clear description of changes

### Code Review

- All PRs require at least one approving review before merging
- Address all feedback from reviewers
- Keep PRs focused and reasonably sized

## Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Purpose |
|--------|---------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `test:` | Adding or updating tests |
| `ci:` | CI/CD changes |
| `refactor:` | Code refactoring |
| `style:` | Code style/formatting |

Examples:
```
feat: add currency conversion fee calculation
fix: handle negative distance in estimate_trip_cost
docs: update installation instructions
test: add edge case tests for get_packing_list
```

## Milestone Tasks (For Team Members)

All tasks directly pertaining to project milestone instructions will be partitioned
among group members during weekly meetings and assigned via GitHub issues within the
project repository. Once assigned, group members will complete tasks locally before
pushing progress to new branches designated for their respective task(s). As tasks are
completed, group members will then create pull requests for their task branch, allowing
progress and potential merge conflicts to be evaluated by the remainder of the group.

## Bug Fixes (For Team Members)

Due to the time-sensitive nature of this project, debugging may occur on a case-by-case
basis. In the case that an issue is identified, the group member who uncovers it is
encouraged to communicate it to the rest of the group. They are also permitted to begin
implementing the fix locally, time permitting. If they are unable to complete the fix
for any reason, the group will deliberate over who is best suited to fulfill the task.

## Code of Conduct

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md). 
By participating, you are expected to uphold this code.

## Questions?

Feel free to open a [GitHub Discussion](https://github.com/UBC-MDS/DSCI_524_group_25/discussions) 
or contact the maintainers.

---

Thank you for contributing to TravelPy!
