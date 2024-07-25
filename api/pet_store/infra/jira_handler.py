from jira import JIRA
from api.pet_store.infra.config_provider import ConfigProvider


class JiraHandler:

    config = ConfigProvider.load_from_file(
        r'C:\Users\Admin\Desktop\Automation_bootcamp\api\pet_store\pet_store.json')

    jira_token = ConfigProvider.load_from_file(
        r'C:\Users\Admin\Desktop\Automation_bootcamp\api\pet_store\secret.json')
    def __init__(self):
        self._jira_url = self.config['jira_url']
        self._auth_jira = JIRA(
            basic_auth=(self.config['jira_mail'], self.jira_token['jira_token']),
            options={'server': self._jira_url})

    def create_issue(self, project_key, summary, description, issuetype='Bus'):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype}
        }

        return self._auth_jira.create_issue(fields=issue_dict)

