class ETLError(Exception):
    """Erro genérico do pipeline ETL."""


class DownloadError(ETLError):
    """Erro ao baixar arquivos da ANS."""


class ExtractionError(ETLError):
    """Erro ao extrair arquivos."""


class NormalizationError(ETLError):
    """Erro ao normalizar estrutura de arquivos."""


class ValidationError(ETLError):
    """Erro de validação de dados."""


class ConsolidationError(ETLError):
    """Erro ao consolidar dados ou persistir no banco."""
