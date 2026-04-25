````md id="pnpm-audit-workflow-00123"
# Security Audit Workflow (pnpm)

Run a security audit on this project using pnpm.

---

## 1. Identify vulnerable packages

```bash
pnpm audit
````

---

## 2. Apply safe updates

```bash
pnpm audit --fix
```

Note: `pnpm audit --fix` is more conservative than npm.
If vulnerabilities are not fixed automatically, update dependencies manually:

```bash
pnpm up --latest
```

Or update specific packages:

```bash
pnpm up <package-name>
```

---

## 3. Run the test suite

```bash
pnpm test
```

---

## 4. Report updates and remaining vulnerabilities

### Check outdated packages

```bash
pnpm outdated
```

### Re-run audit

```bash
pnpm audit
```

---

## Optional (useful for CI/CD)

### Audit only production dependencies

```bash
pnpm audit --prod --fix
```

### Output audit results as JSON

```bash
pnpm audit --json
```

---

## Notes

* pnpm uses a content-addressable store, making dependency resolution stricter.
* It may not automatically fix all vulnerabilities.
* Manual upgrades are often required for transitive (deep) dependencies.

---

```
```
