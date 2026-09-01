# GenLayer Contract Verify

    A wallet-aware GenLayer contract preflight desk for builders. Validate an EVM contract address, inspect wallet and chain context, run a read-only bytecode probe, and demonstrate a clearly labeled transaction lifecycle without signing or moving funds.

    ## Included

    - Injected EVM wallet connect and disconnect flow
    - Account and chain ID detection
    - Bradbury Testnet, Asimov Mainnet, and Local Studio selector
    - EVM address validation and optional read-only eth_getCode check
    - Demo-only Prepare -> Simulate -> Consensus -> Complete lifecycle
    - GenLayer Intelligent Contract for GenLayer Studio
    - Submission PDF and portal checklist

    ## Run locally

    ```bash
    pnpm install
    pnpm dev
    ```

    Then open the Vite URL shown in the terminal. Run `pnpm typecheck` and `pnpm build` before publishing.

    ## GenLayer Studio

    Open [studio.genlayer.com](https://studio.genlayer.com/), paste [contracts/contract_verify.py](contracts/contract_verify.py), and deploy it in the local Studio environment. Call `verify_from_page` with a contract address, public explorer/contract page URL, and network name. The contract uses `gl.nondet.web.get` with `gl.eq_principle.strict_eq` and stores the latest snapshot for `latest_verification`.

    ## Safety

    The browser demo never calls `eth_sendTransaction`, requests a signature, or moves funds. It is intentionally a simulation. Replace the demo provider logic with an official, verified GenLayer RPC endpoint before claiming live network verification.

    ## Repository map

    ```text
    src/                         React frontend
    contracts/contract_verify.py GenLayer Studio contract
    docs/SUBMISSION.md           Portal checklist
    docs/*.pdf                   Reviewer-facing submission packet
    ```

    See [docs/SUBMISSION.md](docs/SUBMISSION.md) for the final GitHub and GenLayer Builder submission checklist.
    