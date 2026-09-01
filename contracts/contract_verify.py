# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class ContractVerifier(gl.Contract):
    """Verifies a contract address against a public page and stores the result.

    The web UI performs the fast browser-side preflight. This Studio contract
    demonstrates the GenLayer-native path: validators independently fetch the
    supplied page and reach strict consensus on whether the normalized address
    is present in the source.
    """

    latest_address: str
    latest_network: str
    latest_status: str
    latest_response_code: u32
    latest_source_url: str
    latest_found: bool

    def __init__(self):
        self.latest_address = ""
        self.latest_network = ""
        self.latest_status = "not_checked"
        self.latest_response_code = 0
        self.latest_source_url = ""
        self.latest_found = False

    @gl.public.write
    def record_verification(
        self,
        contract_address: str,
        network: str,
        status: str,
        response_code: u32,
    ):
        self.latest_address = contract_address
        self.latest_network = network
        self.latest_status = status
        self.latest_response_code = response_code
        self.latest_source_url = ""
        self.latest_found = status == "reachable"

    @gl.public.write
    def verify_from_page(
        self,
        contract_address: str,
        source_url: str,
        network: str,
    ):
        normalized_address = contract_address.lower()

        def fetch_and_check() -> bool:
            page = gl.nondet.web.get(source_url).body.decode("utf-8").lower()
            return normalized_address in page

        found = gl.eq_principle.strict_eq(fetch_and_check)
        self.latest_address = contract_address
        self.latest_network = network
        self.latest_status = "reachable" if found else "not_found"
        self.latest_response_code = 200
        self.latest_source_url = source_url
        self.latest_found = found

    @gl.public.view
    def latest_verification(self) -> str:
        return (
            self.latest_address
            + "|"
            + self.latest_network
            + "|"
            + self.latest_status
            + "|"
            + str(self.latest_response_code)
            + "|"
            + self.latest_source_url
            + "|"
            + str(self.latest_found)
        )