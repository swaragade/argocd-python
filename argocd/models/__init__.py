# coding: utf-8

# flake8: noqa
"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from argocd.models.account_account import AccountAccount
from argocd.models.account_accounts_list import AccountAccountsList
from argocd.models.account_can_i_response import AccountCanIResponse
from argocd.models.account_create_token_request import AccountCreateTokenRequest
from argocd.models.account_create_token_response import AccountCreateTokenResponse
from argocd.models.account_empty_response import AccountEmptyResponse
from argocd.models.account_token import AccountToken
from argocd.models.account_update_password_request import AccountUpdatePasswordRequest
from argocd.models.account_update_password_response import AccountUpdatePasswordResponse
from argocd.models.application_application_manifest_query_with_files import ApplicationApplicationManifestQueryWithFiles
from argocd.models.application_application_manifest_query_with_files_wrapper import ApplicationApplicationManifestQueryWithFilesWrapper
from argocd.models.application_application_patch_request import ApplicationApplicationPatchRequest
from argocd.models.application_application_resource_response import ApplicationApplicationResourceResponse
from argocd.models.application_application_response import ApplicationApplicationResponse
from argocd.models.application_application_rollback_request import ApplicationApplicationRollbackRequest
from argocd.models.application_application_sync_request import ApplicationApplicationSyncRequest
from argocd.models.application_application_sync_window import ApplicationApplicationSyncWindow
from argocd.models.application_application_sync_windows_response import ApplicationApplicationSyncWindowsResponse
from argocd.models.application_file_chunk import ApplicationFileChunk
from argocd.models.application_link_info import ApplicationLinkInfo
from argocd.models.application_links_response import ApplicationLinksResponse
from argocd.models.application_log_entry import ApplicationLogEntry
from argocd.models.application_managed_resources_response import ApplicationManagedResourcesResponse
from argocd.models.application_operation_terminate_response import ApplicationOperationTerminateResponse
from argocd.models.application_resource_actions_list_response import ApplicationResourceActionsListResponse
from argocd.models.application_sync_options import ApplicationSyncOptions
from argocd.models.applicationset_application_set_response import ApplicationsetApplicationSetResponse
from argocd.models.applicationv1alpha1_env_entry import Applicationv1alpha1EnvEntry
from argocd.models.cluster_cluster_id import ClusterClusterID
from argocd.models.cluster_cluster_response import ClusterClusterResponse
from argocd.models.cluster_connector import ClusterConnector
from argocd.models.cluster_dex_config import ClusterDexConfig
from argocd.models.cluster_google_analytics_config import ClusterGoogleAnalyticsConfig
from argocd.models.cluster_help import ClusterHelp
from argocd.models.cluster_oidc_config import ClusterOIDCConfig
from argocd.models.cluster_plugin import ClusterPlugin
from argocd.models.cluster_settings import ClusterSettings
from argocd.models.cluster_settings_plugins_response import ClusterSettingsPluginsResponse
from argocd.models.gpgkey_gnu_pg_public_key_create_response import GpgkeyGnuPGPublicKeyCreateResponse
from argocd.models.gpgkey_gnu_pg_public_key_response import GpgkeyGnuPGPublicKeyResponse
from argocd.models.intstr_int_or_string import IntstrIntOrString
from argocd.models.notification_service import NotificationService
from argocd.models.notification_service_list import NotificationServiceList
from argocd.models.notification_template import NotificationTemplate
from argocd.models.notification_template_list import NotificationTemplateList
from argocd.models.notification_trigger import NotificationTrigger
from argocd.models.notification_trigger_list import NotificationTriggerList
from argocd.models.oidc_claim import OidcClaim
from argocd.models.project_detailed_projects_response import ProjectDetailedProjectsResponse
from argocd.models.project_empty_response import ProjectEmptyResponse
from argocd.models.project_global_projects_response import ProjectGlobalProjectsResponse
from argocd.models.project_project_create_request import ProjectProjectCreateRequest
from argocd.models.project_project_token_create_request import ProjectProjectTokenCreateRequest
from argocd.models.project_project_token_response import ProjectProjectTokenResponse
from argocd.models.project_project_update_request import ProjectProjectUpdateRequest
from argocd.models.project_sync_windows_response import ProjectSyncWindowsResponse
from argocd.models.protobuf_any import ProtobufAny
from argocd.models.repocreds_repo_creds_response import RepocredsRepoCredsResponse
from argocd.models.repository_app_info import RepositoryAppInfo
from argocd.models.repository_directory_app_spec import RepositoryDirectoryAppSpec
from argocd.models.repository_helm_app_spec import RepositoryHelmAppSpec
from argocd.models.repository_helm_chart import RepositoryHelmChart
from argocd.models.repository_helm_charts_response import RepositoryHelmChartsResponse
from argocd.models.repository_kustomize_app_spec import RepositoryKustomizeAppSpec
from argocd.models.repository_manifest_response import RepositoryManifestResponse
from argocd.models.repository_parameter_announcement import RepositoryParameterAnnouncement
from argocd.models.repository_plugin_app_spec import RepositoryPluginAppSpec
from argocd.models.repository_refs import RepositoryRefs
from argocd.models.repository_repo_app_details_query import RepositoryRepoAppDetailsQuery
from argocd.models.repository_repo_app_details_response import RepositoryRepoAppDetailsResponse
from argocd.models.repository_repo_apps_response import RepositoryRepoAppsResponse
from argocd.models.repository_repo_response import RepositoryRepoResponse
from argocd.models.runtime_error import RuntimeError
from argocd.models.runtime_raw_extension import RuntimeRawExtension
from argocd.models.runtime_stream_error import RuntimeStreamError
from argocd.models.session_get_user_info_response import SessionGetUserInfoResponse
from argocd.models.session_session_create_request import SessionSessionCreateRequest
from argocd.models.session_session_response import SessionSessionResponse
from argocd.models.stream_result_of_application_log_entry import StreamResultOfApplicationLogEntry
from argocd.models.stream_result_of_v1alpha1_application_tree import StreamResultOfV1alpha1ApplicationTree
from argocd.models.stream_result_of_v1alpha1_application_watch_event import StreamResultOfV1alpha1ApplicationWatchEvent
from argocd.models.v1_event import V1Event
from argocd.models.v1_event_list import V1EventList
from argocd.models.v1_event_series import V1EventSeries
from argocd.models.v1_event_source import V1EventSource
from argocd.models.v1_fields_v1 import V1FieldsV1
from argocd.models.v1_group_kind import V1GroupKind
from argocd.models.v1_json import V1JSON
from argocd.models.v1_label_selector import V1LabelSelector
from argocd.models.v1_label_selector_requirement import V1LabelSelectorRequirement
from argocd.models.v1_list_meta import V1ListMeta
from argocd.models.v1_load_balancer_ingress import V1LoadBalancerIngress
from argocd.models.v1_managed_fields_entry import V1ManagedFieldsEntry
from argocd.models.v1_micro_time import V1MicroTime
from argocd.models.v1_node_system_info import V1NodeSystemInfo
from argocd.models.v1_object_meta import V1ObjectMeta
from argocd.models.v1_object_reference import V1ObjectReference
from argocd.models.v1_owner_reference import V1OwnerReference
from argocd.models.v1_port_status import V1PortStatus
from argocd.models.v1_time import V1Time
from argocd.models.v1alpha1_aws_auth_config import V1alpha1AWSAuthConfig
from argocd.models.v1alpha1_app_project import V1alpha1AppProject
from argocd.models.v1alpha1_app_project_list import V1alpha1AppProjectList
from argocd.models.v1alpha1_app_project_spec import V1alpha1AppProjectSpec
from argocd.models.v1alpha1_app_project_status import V1alpha1AppProjectStatus
from argocd.models.v1alpha1_application import V1alpha1Application
from argocd.models.v1alpha1_application_condition import V1alpha1ApplicationCondition
from argocd.models.v1alpha1_application_destination import V1alpha1ApplicationDestination
from argocd.models.v1alpha1_application_list import V1alpha1ApplicationList
from argocd.models.v1alpha1_application_match_expression import V1alpha1ApplicationMatchExpression
from argocd.models.v1alpha1_application_preserved_fields import V1alpha1ApplicationPreservedFields
from argocd.models.v1alpha1_application_set import V1alpha1ApplicationSet
from argocd.models.v1alpha1_application_set_application_status import V1alpha1ApplicationSetApplicationStatus
from argocd.models.v1alpha1_application_set_condition import V1alpha1ApplicationSetCondition
from argocd.models.v1alpha1_application_set_generator import V1alpha1ApplicationSetGenerator
from argocd.models.v1alpha1_application_set_list import V1alpha1ApplicationSetList
from argocd.models.v1alpha1_application_set_nested_generator import V1alpha1ApplicationSetNestedGenerator
from argocd.models.v1alpha1_application_set_resource_ignore_differences import V1alpha1ApplicationSetResourceIgnoreDifferences
from argocd.models.v1alpha1_application_set_rollout_step import V1alpha1ApplicationSetRolloutStep
from argocd.models.v1alpha1_application_set_rollout_strategy import V1alpha1ApplicationSetRolloutStrategy
from argocd.models.v1alpha1_application_set_spec import V1alpha1ApplicationSetSpec
from argocd.models.v1alpha1_application_set_status import V1alpha1ApplicationSetStatus
from argocd.models.v1alpha1_application_set_strategy import V1alpha1ApplicationSetStrategy
from argocd.models.v1alpha1_application_set_sync_policy import V1alpha1ApplicationSetSyncPolicy
from argocd.models.v1alpha1_application_set_template import V1alpha1ApplicationSetTemplate
from argocd.models.v1alpha1_application_set_template_meta import V1alpha1ApplicationSetTemplateMeta
from argocd.models.v1alpha1_application_source import V1alpha1ApplicationSource
from argocd.models.v1alpha1_application_source_directory import V1alpha1ApplicationSourceDirectory
from argocd.models.v1alpha1_application_source_helm import V1alpha1ApplicationSourceHelm
from argocd.models.v1alpha1_application_source_jsonnet import V1alpha1ApplicationSourceJsonnet
from argocd.models.v1alpha1_application_source_kustomize import V1alpha1ApplicationSourceKustomize
from argocd.models.v1alpha1_application_source_plugin import V1alpha1ApplicationSourcePlugin
from argocd.models.v1alpha1_application_source_plugin_parameter import V1alpha1ApplicationSourcePluginParameter
from argocd.models.v1alpha1_application_spec import V1alpha1ApplicationSpec
from argocd.models.v1alpha1_application_status import V1alpha1ApplicationStatus
from argocd.models.v1alpha1_application_summary import V1alpha1ApplicationSummary
from argocd.models.v1alpha1_application_tree import V1alpha1ApplicationTree
from argocd.models.v1alpha1_application_watch_event import V1alpha1ApplicationWatchEvent
from argocd.models.v1alpha1_backoff import V1alpha1Backoff
from argocd.models.v1alpha1_basic_auth_bitbucket_server import V1alpha1BasicAuthBitbucketServer
from argocd.models.v1alpha1_bearer_token_bitbucket_cloud import V1alpha1BearerTokenBitbucketCloud
from argocd.models.v1alpha1_chart_details import V1alpha1ChartDetails
from argocd.models.v1alpha1_cluster import V1alpha1Cluster
from argocd.models.v1alpha1_cluster_cache_info import V1alpha1ClusterCacheInfo
from argocd.models.v1alpha1_cluster_config import V1alpha1ClusterConfig
from argocd.models.v1alpha1_cluster_generator import V1alpha1ClusterGenerator
from argocd.models.v1alpha1_cluster_info import V1alpha1ClusterInfo
from argocd.models.v1alpha1_cluster_list import V1alpha1ClusterList
from argocd.models.v1alpha1_command import V1alpha1Command
from argocd.models.v1alpha1_compared_to import V1alpha1ComparedTo
from argocd.models.v1alpha1_config_management_plugin import V1alpha1ConfigManagementPlugin
from argocd.models.v1alpha1_connection_state import V1alpha1ConnectionState
from argocd.models.v1alpha1_duck_type_generator import V1alpha1DuckTypeGenerator
from argocd.models.v1alpha1_exec_provider_config import V1alpha1ExecProviderConfig
from argocd.models.v1alpha1_git_directory_generator_item import V1alpha1GitDirectoryGeneratorItem
from argocd.models.v1alpha1_git_file_generator_item import V1alpha1GitFileGeneratorItem
from argocd.models.v1alpha1_git_generator import V1alpha1GitGenerator
from argocd.models.v1alpha1_gnu_pg_public_key import V1alpha1GnuPGPublicKey
from argocd.models.v1alpha1_gnu_pg_public_key_list import V1alpha1GnuPGPublicKeyList
from argocd.models.v1alpha1_health_status import V1alpha1HealthStatus
from argocd.models.v1alpha1_helm_file_parameter import V1alpha1HelmFileParameter
from argocd.models.v1alpha1_helm_parameter import V1alpha1HelmParameter
from argocd.models.v1alpha1_host_info import V1alpha1HostInfo
from argocd.models.v1alpha1_host_resource_info import V1alpha1HostResourceInfo
from argocd.models.v1alpha1_info import V1alpha1Info
from argocd.models.v1alpha1_info_item import V1alpha1InfoItem
from argocd.models.v1alpha1_jwt_token import V1alpha1JWTToken
from argocd.models.v1alpha1_jwt_tokens import V1alpha1JWTTokens
from argocd.models.v1alpha1_jsonnet_var import V1alpha1JsonnetVar
from argocd.models.v1alpha1_known_type_field import V1alpha1KnownTypeField
from argocd.models.v1alpha1_kustomize_gvk import V1alpha1KustomizeGvk
from argocd.models.v1alpha1_kustomize_options import V1alpha1KustomizeOptions
from argocd.models.v1alpha1_kustomize_patch import V1alpha1KustomizePatch
from argocd.models.v1alpha1_kustomize_replica import V1alpha1KustomizeReplica
from argocd.models.v1alpha1_kustomize_res_id import V1alpha1KustomizeResId
from argocd.models.v1alpha1_kustomize_selector import V1alpha1KustomizeSelector
from argocd.models.v1alpha1_list_generator import V1alpha1ListGenerator
from argocd.models.v1alpha1_managed_namespace_metadata import V1alpha1ManagedNamespaceMetadata
from argocd.models.v1alpha1_matrix_generator import V1alpha1MatrixGenerator
from argocd.models.v1alpha1_merge_generator import V1alpha1MergeGenerator
from argocd.models.v1alpha1_operation import V1alpha1Operation
from argocd.models.v1alpha1_operation_initiator import V1alpha1OperationInitiator
from argocd.models.v1alpha1_operation_state import V1alpha1OperationState
from argocd.models.v1alpha1_orphaned_resource_key import V1alpha1OrphanedResourceKey
from argocd.models.v1alpha1_orphaned_resources_monitor_settings import V1alpha1OrphanedResourcesMonitorSettings
from argocd.models.v1alpha1_override_ignore_diff import V1alpha1OverrideIgnoreDiff
from argocd.models.v1alpha1_plugin_config_map_ref import V1alpha1PluginConfigMapRef
from argocd.models.v1alpha1_plugin_generator import V1alpha1PluginGenerator
from argocd.models.v1alpha1_plugin_input import V1alpha1PluginInput
from argocd.models.v1alpha1_project_role import V1alpha1ProjectRole
from argocd.models.v1alpha1_pull_request_generator import V1alpha1PullRequestGenerator
from argocd.models.v1alpha1_pull_request_generator_azure_dev_ops import V1alpha1PullRequestGeneratorAzureDevOps
from argocd.models.v1alpha1_pull_request_generator_bitbucket import V1alpha1PullRequestGeneratorBitbucket
from argocd.models.v1alpha1_pull_request_generator_bitbucket_server import V1alpha1PullRequestGeneratorBitbucketServer
from argocd.models.v1alpha1_pull_request_generator_filter import V1alpha1PullRequestGeneratorFilter
from argocd.models.v1alpha1_pull_request_generator_git_lab import V1alpha1PullRequestGeneratorGitLab
from argocd.models.v1alpha1_pull_request_generator_gitea import V1alpha1PullRequestGeneratorGitea
from argocd.models.v1alpha1_pull_request_generator_github import V1alpha1PullRequestGeneratorGithub
from argocd.models.v1alpha1_repo_creds import V1alpha1RepoCreds
from argocd.models.v1alpha1_repo_creds_list import V1alpha1RepoCredsList
from argocd.models.v1alpha1_repository import V1alpha1Repository
from argocd.models.v1alpha1_repository_certificate import V1alpha1RepositoryCertificate
from argocd.models.v1alpha1_repository_certificate_list import V1alpha1RepositoryCertificateList
from argocd.models.v1alpha1_repository_list import V1alpha1RepositoryList
from argocd.models.v1alpha1_resource_action import V1alpha1ResourceAction
from argocd.models.v1alpha1_resource_action_param import V1alpha1ResourceActionParam
from argocd.models.v1alpha1_resource_diff import V1alpha1ResourceDiff
from argocd.models.v1alpha1_resource_ignore_differences import V1alpha1ResourceIgnoreDifferences
from argocd.models.v1alpha1_resource_networking_info import V1alpha1ResourceNetworkingInfo
from argocd.models.v1alpha1_resource_node import V1alpha1ResourceNode
from argocd.models.v1alpha1_resource_override import V1alpha1ResourceOverride
from argocd.models.v1alpha1_resource_ref import V1alpha1ResourceRef
from argocd.models.v1alpha1_resource_result import V1alpha1ResourceResult
from argocd.models.v1alpha1_resource_status import V1alpha1ResourceStatus
from argocd.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from argocd.models.v1alpha1_revision_history import V1alpha1RevisionHistory
from argocd.models.v1alpha1_revision_metadata import V1alpha1RevisionMetadata
from argocd.models.v1alpha1_scm_provider_generator import V1alpha1SCMProviderGenerator
from argocd.models.v1alpha1_scm_provider_generator_aws_code_commit import V1alpha1SCMProviderGeneratorAWSCodeCommit
from argocd.models.v1alpha1_scm_provider_generator_azure_dev_ops import V1alpha1SCMProviderGeneratorAzureDevOps
from argocd.models.v1alpha1_scm_provider_generator_bitbucket import V1alpha1SCMProviderGeneratorBitbucket
from argocd.models.v1alpha1_scm_provider_generator_bitbucket_server import V1alpha1SCMProviderGeneratorBitbucketServer
from argocd.models.v1alpha1_scm_provider_generator_filter import V1alpha1SCMProviderGeneratorFilter
from argocd.models.v1alpha1_scm_provider_generator_gitea import V1alpha1SCMProviderGeneratorGitea
from argocd.models.v1alpha1_scm_provider_generator_github import V1alpha1SCMProviderGeneratorGithub
from argocd.models.v1alpha1_scm_provider_generator_gitlab import V1alpha1SCMProviderGeneratorGitlab
from argocd.models.v1alpha1_secret_ref import V1alpha1SecretRef
from argocd.models.v1alpha1_signature_key import V1alpha1SignatureKey
from argocd.models.v1alpha1_sync_operation import V1alpha1SyncOperation
from argocd.models.v1alpha1_sync_operation_resource import V1alpha1SyncOperationResource
from argocd.models.v1alpha1_sync_operation_result import V1alpha1SyncOperationResult
from argocd.models.v1alpha1_sync_policy import V1alpha1SyncPolicy
from argocd.models.v1alpha1_sync_policy_automated import V1alpha1SyncPolicyAutomated
from argocd.models.v1alpha1_sync_status import V1alpha1SyncStatus
from argocd.models.v1alpha1_sync_strategy import V1alpha1SyncStrategy
from argocd.models.v1alpha1_sync_strategy_apply import V1alpha1SyncStrategyApply
from argocd.models.v1alpha1_sync_strategy_hook import V1alpha1SyncStrategyHook
from argocd.models.v1alpha1_sync_window import V1alpha1SyncWindow
from argocd.models.v1alpha1_tls_client_config import V1alpha1TLSClientConfig
from argocd.models.v1alpha1_tag_filter import V1alpha1TagFilter
from argocd.models.version_version_message import VersionVersionMessage
