import httpx
from app.core.logging import log

ANS_BASE_URL = "https://dadosabertos.ans.gov.br/FTP/PDA"


class ANSClient:
    def listar_diretorios(self) -> list[str]:
        """
        Lista diretórios disponíveis na ANS.
        Aqui simplificado: assume que os ZIPs já seguem padrão trimestral.
        """
        log.info("Consultando estrutura pública da ANS")
        
        return []
