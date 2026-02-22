import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from healthChecker import HealthChecker, check_database, check_cache, check_external_api

class TestHealthChecker:
    @pytest.fixture
    def checker(self):
        hc = HealthChecker()
        hc.register_check('database', check_database)
        hc.register_check('cache', check_cache)
        hc.register_check('external_api', check_external_api)
        return hc

    def test_healthy_check(self, checker):
        result = checker.run_check('database')
        assert result['status'] == 'healthy'

    def test_unhealthy_check(self, checker):
        result = checker.run_check('external_api')
        assert result['status'] == 'unhealthy'

    def test_overall_degraded(self, checker):
        result = checker.run_all()
        assert result['status'] == 'degraded', "1 of 3 failing = degraded"

    def test_response_time_tracked(self, checker):
        result = checker.run_check('database')
        assert 'response_time_ms' in result
        assert result['response_time_ms'] > 0
