import os

from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-pro")

file_num_limit = 50
file_lines_limit = 200

processed_files_count = 0


def get_project_summary(file_summaries):
    message = (
        "I will give you the filepath and summaries of all files in a project. I want you to write me a summary of the whole project. E.g write me a README.md for the project. The files summary: "
        + str(file_summaries)
    )
    res = model.invoke(message)
    return res


def get_all_file_paths(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


def get_file_summary(file_path):
    f = open(file_path, "r")
    contents = f.read()
    message = (
        "I will give you the contents of a file and I want you to return me the summary of its content in plain text. No paragraphs and no bullet points. The file content is: "
        + contents
    )
    res = model.invoke(message)
    return res


# directory = "/Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy"
# file_paths = get_all_file_paths(directory)
# file_summaries = {}
# for file_path in file_paths:
#     # print(file_path)
#     file_summary = get_file_summary(file_path)
#     file_summaries[file_path] = file_summary
#     print("# " + file_path + ": " + file_summary + "\n")

file_summaries = """
# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/go.mod: This go module contains the Terraform provider for Stackit, a cloud computing provider. It allows users to interact with Stackit's services, such as argus, dns, loadbalancer, logme, mariadb, mongodbflex, objectstorage, opensearch, postgresflex, postgresql, rabbitmq, redis, resourcemanager, secretsmanager, ske, and virtualmachines, through Terraform. The provider is compatible with Terraform v1.7.0 and uses the Terraform plugin framework v1.7.0 and validators v0.12.0.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/.goreleaser.yaml: This file contains the build configuration for goreleaser. It specifies the build environment, flags, and artifacts to create. The builds section defines the platforms and architectures for which the software will be built, and includes options for setting environment variables, mod timestamps, flags, and ldflags. The archives section specifies the format and naming template for the archives to be created. The checksum section defines the algorithm and extra files to be included in the checksum. The signs section specifies the artifacts to be signed and the signing arguments. The release section defines extra files to be included in the release and whether the release should be marked as a draft. The changelog section specifies whether to skip creating a changelog.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/Makefile: Defines scripts to assist with project setup, linting, documentation generation, building, and testing a Terraform provider. Includes tasks for running acceptance tests with environmental variables.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/terraform-registry-manifest.json: The file contains a single JSON object with two keys: "version" and "metadata". The value of "version" is 1. The value of "metadata" is another JSON object with a single key: "protocol_versions". The value of "protocol_versions" is a list containing a single string: "6.0".

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/golang-ci.yaml: This file contains configuration options for analysis running, including concurrency, timeout, and linter settings. Linters can be enabled or disabled, and some have specific configurations, such as error messages for blacklisted packages or ignored rules. The file also includes settings for issue exclusion.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/NOTICE.txt: Terraform provider for STACKIT managed infrastructure by Schwarz IT GmBH & Co. KG

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/main.go: Terraform provider for stackit written in Go using HashiCorp's Terraform Plugin Framework.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/provider.go: This Terraform provider allows you to interact with the Stackit Platform.

It supports managing Argus, DNS, Load Balancer, LogMe, MariaDB, MongoDB Flex, Object Storage, OpenSearch, PostgreSQL, PostgreSQL Flex, RabbitMQ, Redis, Secrets Manager, and Kubernetes Engine resources. The provider also supports managing Credentials, Credentials Groups, Instances, Projects, Record Sets, and Scrape Configs.

The configuration options for the provider include credentials path, service account email, service account key, private key, private key path, token, region, custom endpoints for various services, and custom endpoints for the token and JWKS APIs. The provider supports both key and token-based authentication methods.

The data sources provided by the provider allow you to retrieve information about existing resources without modifying them. The resources provided by the provider allow you to create, update, and delete resources within the Stackit Platform.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/validate/validate.go: Provides a UUID validation function.
Provides an IP validation function.
Provides a record set validation function.
Provides a validation function for values that must not contain the identifier separator.
Provides a validation function for minor version numbers.
Provides a validation function for RFC3339 format with seconds only.
Provides a validation function for CIDR notation.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/core/core.go: ProviderData is a package that contains:
- A DiagsToError function that converts diagnostics' errors into an error with a human-readable description.
- A LogAndAddError function that logs the error and adds it to the diags.
- A LogAndAddWarning function that logs the warning and adds it to the diags.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/conversion/conversion.go: converts between types in Terraform plugins, including converting to and from strings, maps of strings, and pointers to primitive types.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/objectstorage/credentialsgroup/resource.go: ObjectStorage credentials group schema. Must have a `region` specified in the provider configuration. If you are creating `credentialsgroup` and `bucket` resources simultaneously, please include the `depends_on` field so that they are created sequentially. This prevents errors from concurrent calls to the service enablement that is done in the background.

Terraform's internal data source identifier. It is structured as "`project_id`,`credentials_group_id`".

The credentials group's display name.

Project ID to which the credentials group is associated.

Credentials group uniform resource name (URN)

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/objectstorage/credentialsgroup/datasource.go: ObjectStorage credentials group data source schema. Must have a `region` specified in the provider configuration. Returns credentials group information by name or by credentials group ID.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/objectstorage/credential/resource.go: The credential resource manages object storage credentials within STACKIT. It allows you to create, read, update, and delete credentials. Each credential has a unique ID, a project ID, a credentials group ID, and an expiration timestamp. The access key and secret access key are generated when the credential is created and cannot be modified.

The resource schema includes the following attributes:

* `id`: The Terraform-generated resource ID. It is structured as "`project_id`,`credentials_group_id`,`credential_id`".
* `credential_id`: The credential ID.
* `credentials_group_id`: The credentials group ID.
* `project_id`: The STACKIT Project ID to which the credential group is associated.
* `name`: The credential name.
* `access_key`: The access key.
* `secret_access_key`: The secret access key.
* `expiration_timestamp`: The expiration timestamp, in RFC3339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/objectstorage/credential/datasource.go: ObjectStorage credential data source schema.

* `id` - Terraform's internal resource identifier. It is structured as "`project_id`,`credentials_group_id`,`credential_id`".
* `credential_id` - The credential ID.
* `credentials_group_id` - The credential group ID.
* `project_id` - STACKIT Project ID to which the credential group is associated.
* `name` - The credential name.
* `access_key` - The access key.
* `secret_access_key` - The secret access key.
* `expiration_timestamp` - The expiration timestamp.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/objectstorage/bucket/resource.go: ObjectStorage bucket resource schema. Must have a `region` specified in the provider configuration. If you are creating `credentialsgroup` and `bucket` resources simultaneously, please include the `depends_on` field so that they are created sequentially. This prevents errors from concurrent calls to the service enablement that is done in the background.

This resource has the following attributes:

- `id`: Terraform's internal resource identifier. It is structured as "`project_id`,`name`".
- `name`: The bucket name. It must be DNS conform.
- `project_id`: STACKIT Project ID to which the bucket is associated.
- `url_path_style`: URL in path style.
- `url_virtual_hosted_style`: URL in virtual hosted style.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/objectstorage/bucket/datasource.go: This data source returns information about an existing ObjectStorage bucket.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/ske/cluster/resource.go: SKE Cluster resource schema. Must have a `region` specified in the provider configuration.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/ske/cluster/datasource.go: SKE Cluster data source represents a Kubernetes cluster on STACKIT. It supports a variety of features for managing and controlling the cluster. The data source can be used to retrieve information about a cluster, including its name, Kubernetes version, node pools, maintenance settings, hiberation settings, and more. With the data source, you can easily access and utilize the information about your SKE cluster within your Terraform configurations.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/ske/project/resource.go: The SKE project resource allows you to enable the SKE service and you can only have one per project. Before deleting this resource, all SKE clusters associated to the project must be deleted. Warning: SKE project resource is no longer in use and will be removed with the next minor release. SKE service enablement is done automatically when a new cluster is created.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/ske/project/datasource.go: The project data source provides information about SKE projects. It has the following attributes:

- id: Terraform's internal data source. ID. It is structured as "`project_id`".
- project_id: STACKIT Project ID in which the kubernetes project is enabled.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/ske/kubeconfig/resource.go: This resource allows you to manage SKE kubeconfigs.
It supports the following actions:

- Create
- Read
- Delete

The following attributes are supported:

- `id`: Terraform's internal resource ID. It is structured as "`project_id`,`cluster_name`,`kube_config_id`".
- `kube_config_id`: Internally generated UUID to identify a kubeconfig resource in Terraform, since the SKE API doesnt return a kubeconfig identifier
- `cluster_name`: Name of the SKE cluster.
- `project_id`: STACKIT project ID to which the cluster is associated.
- `kube_config`: Raw short-lived admin kubeconfig.
- `expiration`: Expiration time of the kubeconfig, in seconds.
- `expires_at`: Timestamp when the kubeconfig expires
- `refresh`: If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/mongodbflex/user/resource.go: This resource allows you to manage MongoDB Flex users.

The following attributes are required:

* instance_id - The ID of the MongoDB Flex instance.
* project_id - The STACKIT project ID to which the instance is associated.
* roles - The database access levels for the user.
* database - The database to which the user will have access.

The following attributes are optional:

* username - The username for the user.
* password - The password for the user. This attribute is sensitive and will not be displayed in the Terraform state.

The following attributes are computed:

* id - The ID of the user. This is structured as "`project_id`,`instance_id`,`user_id`".
* user_id - The ID of the user.
* host - The hostname of the MongoDB Flex instance.
* port - The port number of the MongoDB Flex instance.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/mongodbflex/user/datasource.go: MongoDB Flex user data source schema. Must have a `region` specified in the provider configuration.

`id` - Terraform's internal data source. ID. It is structured as "`project_id`,`instance_id`,`user_id`".
`user_id` - User ID.
`instance_id` - ID of the MongoDB Flex instance.
`project_id` - STACKIT project ID to which the instance is associated.
`username` - MongoDB user username.
`roles` - List of MongoDB user roles.
`database` - MongoDB database to which the user is associated to.
`host` - MongoDB instance hostname.
`port` - MongoDB instance port.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/mongodbflex/instance/resource.go: Summary
-------
- Resource for managing MongoDB Flex instances.
- Create, read, update, delete, and import state.
- CRUD operations trigger API calls to MongoDB Flex.
- Supports ACL management, backup schedules, flavor selection, replica count, storage configuration, version specification, and custom options.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/mongodbflex/instance/datasource.go: MongoDB Flex instance data source schema. Must have a `region` specified in the provider configuration.

The datasource returns the following attributes:

- `id` - Terraform's internal data source. ID. It is structured as "`project_id`, `instance_id`".
- `instance_id` - ID of the MongoDB Flex instance.
- `project_id` - STACKIT project ID to which the instance is associated.
- `name` - Instance name.
- `acl` - The Access Control List (ACL) for the MongoDB Flex instance.
- `backup_schedule` - The backup schedule. Should follow the cron scheduling system format (e.g. "0 0 * * *").
- `flavor` - Nested attribute block.
-- `flavor.id` - ID of the MongoDB Flex flavor.
-- `flavor.description` - Description of the MongoDB Flex flavor.
-- `flavor.cpu` - Number of CPUs for the MongoDB Flex instance.
-- `flavor.ram` - Amount of memory for the MongoDB Flex instance.
- `replicas` - Number of replicas for the MongoDB Flex instance.
- `storage` - Nested attribute block.
-- `storage.class` - Class of storage for the MongoDB Flex instance.
-- `storage.size` - Size of storage for the MongoDB Flex instance.
- `version` - Version of MongoDB running on the instance.
- `options` - Nested attribute block.
-- `options.type` - Type of options.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/loadbalancer/credential/resource.go: Load balancer credential resource schema. Must have a `region` specified in the provider configuration.

The Terraform's internal resource ID. It is structured as "`project_id`\",\"`credentials_ref`\"".

The credentials reference can be used for observability of the Load Balancer.

STACKIT project ID to which the load balancer credential is associated.

Credential name.

The username used for the ARGUS instance.

The password used for the ARGUS instance.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/loadbalancer/loadbalancer/resource.go: This resource manages Load Balancers and allows to create, read, update and delete Load Balancers.

It is important to note that before Load Balancer can be created the load balancer functionality via API needs to be enabled. This is not required by Terraform and needs to be done manually.

The following code sample shows you how to use the resource:
```go
package main

import (
	"context"

	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/plugin"
	"github.com/stackitcloud/terraform-provider-stackit/stackit"
)

func main() {
	plugin.Serve(&plugin.ServeOpts{
		ProviderFunc: func() *schema.Provider {
			return stackit.Provider()
		},
	})
}
```

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/loadbalancer/loadbalancer/datasource.go: This data source retrieves information about an existing load balancer. The schema includes:
- project_id: STACKIT project ID to which the Load Balancer is associated. Required and must be a UUID.
- external_address: Load balancer's external address. Computed and read only.
- id: Terraform internal resource ID. Computed and read only.
- listeners: List of objects, which represent the listener configuration for load balancer. Computed.
- name: Name of the Load Balancer. Required. Length between 1-63, alphanumeric. Cannot have special characters or start or end with a hyphen.
- network: List of objects which represents network configuration of the load balancer. Computed and read-only.
- options: Load Balancer optional settings. Computed and read-only.
- private_address: Load balancer's private address. Computed and read-only.
- target_pools: List of objects which represents target pools configuration of the load balancer. Computed and read-only.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/dns/recordset/resource.go: - package dns
- import (
  - "context"
  - "fmt"
  - "strings"

  - "github.com/hashicorp/terraform-plugin-framework-validators/int64validator"
  - "github.com/hashicorp/terraform-plugin-framework-validators/listvalidator"
  - "github.com/hashicorp/terraform-plugin-framework-validators/stringvalidator"
  - "github.com/hashicorp/terraform-plugin-framework/attr"
  - "github.com/hashicorp/terraform-plugin-framework/path"
  - "github.com/hashicorp/terraform-plugin-framework/resource"
  - "github.com/hashicorp/terraform-plugin-framework/resource/schema"
  - "github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
  - "github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
  - "github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
  - "github.com/hashicorp/terraform-plugin-framework/schema/validator"
  - "github.com/hashicorp/terraform-plugin-framework/types"
  - "github.com/hashicorp/terraform-plugin-log/tflog"
  - "github.com/stackitcloud/stackit-sdk-go/core/config"
  - "github.com/stackitcloud/stackit-sdk-go/services/dns"
  - "github.com/stackitcloud/stackit-sdk-go/services/dns/wait"
  - "github.com/stackitcloud/terraform-provider-stackit/stackit/internal/conversion"
  - "github.com/stackitcloud/terraform-provider-stackit/stackit/internal/core"
  - "github.com/stackitcloud/terraform-provider-stackit/stackit/internal/validate"
)

- // Ensure the implementation satisfies the expected interfaces.
- var (
  - _ resource.Resource                = &recordSetResource{}
  - _ resource.ResourceWithConfigure   = &recordSetResource{}
  - _ resource.ResourceWithImportState = &recordSetResource{}
)

- type Model struct {
  - Id          types.String `tfsdk:"id"` // needed by TF
  - RecordSetId types.String `tfsdk:"record_set_id"`
  - ZoneId      types.String `tfsdk:"zone_id"`
  - ProjectId   types.String `tfsdk:"project_id"`
  - Active      types.Bool   `tfsdk:"active"`
  - Comment     types.String `tfsdk:"comment"`
  - Name        types.String `tfsdk:"name"`
  - Records     types.List   `tfsdk:"records"`
  - TTL         types.Int64  `tfsdk:"ttl"`
  - Type        types.String `tfsdk:"type"`
  - Error       types.String `tfsdk:"error"`
  - State       types.String `tfsdk:"state"`
  - FQDN        types.String `tfsdk:"fqdn"`
}

- // NewRecordSetResource is a helper function to simplify the provider implementation.
- func NewRecordSetResource() resource.Resource {
  - return &recordSetResource{}
}

- // recordSetResource is the resource implementation.
- type recordSetResource struct {
  - client *dns.APIClient
}

- // Metadata returns the resource type name.
- func (r *recordSetResource) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
  - resp.TypeName = req.ProviderTypeName + "_dns_record_set"
}

- // Configure adds the provider configured client to the resource.
- func (r *recordSetResource) Configure(ctx context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
  - // Prevent panic if the provider has not been configured.
  - if req.ProviderData == nil {
    - return
  }

  - providerData, ok := req.ProviderData.(core.ProviderData)
  - if !ok {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error configuring API client", fmt.Sprintf("Expected configure type stackit.ProviderData, got %T", req.ProviderData))
    - return
  }

  - var apiClient *dns.APIClient
  - var err error
  - if providerData.DnsCustomEndpoint != "" {
    - apiClient, err = dns.NewAPIClient(
      - config.WithCustomAuth(providerData.RoundTripper),
      - config.WithEndpoint(providerData.DnsCustomEndpoint),
    - )
  - } else {
    - apiClient, err = dns.NewAPIClient(
      - config.WithCustomAuth(providerData.RoundTripper),
    - )
  }

  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error configuring API client", fmt.Sprintf("Configuring client: %v. This is an error related to the provider configuration, not to the resource configuration", err))
    - return
  }

  - r.client = apiClient
  - tflog.Info(ctx, "DNS record set client configured")
}

- // Schema defines the schema for the resource.
- func (r *recordSetResource) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
  - resp.Schema = schema.Schema{
    - Description: "DNS Record Set Resource schema.",
    - Attributes: map[string]schema.Attribute{
      - "id": schema.StringAttribute{
        - Description: "Terraform's internal resource ID. It is structured as \"`project_id`,`zone_id`,`record_set_id`\".",
        - Computed:    true,
        - PlanModifiers: []planmodifier.String{
          - stringplanmodifier.UseStateForUnknown(),
        },
      },
      - "project_id": schema.StringAttribute{
        - Description: "STACKIT project ID to which the dns record set is associated.",
        - Required:    true,
        - PlanModifiers: []planmodifier.String{
          - stringplanmodifier.RequiresReplace(),
        },
        - Validators: []validator.String{
          - validate.UUID(),
          - validate.NoSeparator(),
        },
      },
      - "zone_id": schema.StringAttribute{
        - Description: "The zone ID to which is dns record set is associated.",
        - Required:    true,
        - PlanModifiers: []planmodifier.String{
          - stringplanmodifier.RequiresReplace(),
        },
        - Validators: []validator.String{
          - validate.UUID(),
          - validate.NoSeparator(),
        },
      },
      - "record_set_id": schema.StringAttribute{
        - Description: "The rr set id.",
        - Computed:    true,
        - PlanModifiers: []planmodifier.String{
          - stringplanmodifier.UseStateForUnknown(),
        },
        - Validators: []validator.String{
          - validate.UUID(),
          - validate.NoSeparator(),
        },
      },
      - "name": schema.StringAttribute{
        - Description: "Name of the record which should be a valid domain according to rfc1035 Section 2.3.4. E.g. `example.com`",
        - Required:    true,
        - Validators: []validator.String{
          - stringvalidator.LengthAtLeast(1),
          - stringvalidator.LengthAtMost(63),
        },
      },
      - "fqdn": schema.StringAttribute{
        - Description: "Fully qualified domain name (FQDN) of the record set.",
        - Computed:    true,
      },
      - "records": schema.ListAttribute{
        - Description: "Records.",
        - ElementType: types.StringType,
        - Required:    true,
        - Validators: []validator.List{
          - listvalidator.SizeAtLeast(1),
          - listvalidator.UniqueValues(),
          - listvalidator.ValueStringsAre(validate.RecordSet()),
        },
      },
      - "ttl": schema.Int64Attribute{
        - Description: "Time to live. E.g. 3600",
        - Optional:    true,
        - Computed:    true,
        - Validators: []validator.Int64{
          - int64validator.AtLeast(60),
          - int64validator.AtMost(99999999),
        },
      },
      - "type": schema.StringAttribute{
        - Description: "The record set type. E.g. `A` or `CNAME`",
        - Optional:    true,
        - Computed:    true,
        - PlanModifiers: []planmodifier.String{
          - stringplanmodifier.UseStateForUnknown(),
        },
      },
      - "active": schema.BoolAttribute{
        - Description: "Specifies if the record set is active or not.",
        - Optional:    true,
        - Computed:    true,
        - Default:     booldefault.StaticBool(true),
      },
      - "comment": schema.StringAttribute{
        - Description: "Comment.",
        - Optional:    true,
        - Computed:    true,
        - Validators: []validator.String{
          - stringvalidator.LengthAtMost(255),
        },
      },
      - "error": schema.StringAttribute{
        - Description: "Error shows error in case create/update/delete failed.",
        - Computed:    true,
        - Validators: []validator.String{
          - stringvalidator.LengthAtMost(2000),
        },
      },
      - "state": schema.StringAttribute{
        - Description: "Record set state.",
        - Computed:    true,
      },
    },
  }
}

- // Create creates the resource and sets the initial Terraform state.
- func (r *recordSetResource) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) { // nolint:gocritic // function signature required by Terraform
  - // Retrieve values from plan
  - var model Model
  - diags := req.Plan.Get(ctx, &model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }

  - projectId := model.ProjectId.ValueString()
  - zoneId := model.ZoneId.ValueString()
  - ctx = tflog.SetField(ctx, "project_id", projectId)
  - ctx = tflog.SetField(ctx, "zone_id", zoneId)

  - // Generate API request body from model
  - payload, err := toCreatePayload(&model)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error creating record set", fmt.Sprintf("Creating API payload: %v", err))
    - return
  }
  - // Create new recordset
  - recordSetResp, err := r.client.CreateRecordSet(ctx, projectId, zoneId).CreateRecordSetPayload(*payload).Execute()
  - if err != nil || recordSetResp.Rrset == nil || recordSetResp.Rrset.Id == nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error creating record set", fmt.Sprintf("Calling API: %v", err))
    - return
  }
  - ctx = tflog.SetField(ctx, "record_set_id", *recordSetResp.Rrset.Id)

  - waitResp, err := wait.CreateRecordSetWaitHandler(ctx, r.client, projectId, zoneId, *recordSetResp.Rrset.Id).WaitWithContext(ctx)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error creating record set", fmt.Sprintf("Instance creation waiting: %v", err))
    - return
  }

  - // Map response body to schema
  - err = mapFields(waitResp, &model)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error creating record set", fmt.Sprintf("Processing API payload: %v", err))
    - return
  }
  - // Set state to fully populated data
  - diags = resp.State.Set(ctx, model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }
  - tflog.Info(ctx, "DNS record set created")
}

- // Read refreshes the Terraform state with the latest data.
- func (r *recordSetResource) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) { // nolint:gocritic // function signature required by Terraform
  - var model Model
  - diags := req.State.Get(ctx, &model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }
  - projectId := model.ProjectId.ValueString()
  - zoneId := model.ZoneId.ValueString()
  - recordSetId := model.RecordSetId.ValueString()
  - ctx = tflog.SetField(ctx, "project_id", projectId)
  - ctx = tflog.SetField(ctx, "zone_id", zoneId)
  - ctx = tflog.SetField(ctx, "record_set_id", recordSetId)

  - recordSetResp, err := r.client.GetRecordSet(ctx, projectId, zoneId, recordSetId).Execute()
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error reading record set", fmt.Sprintf("Calling API: %v", err))
    - return
  }

  - // Map response body to schema
  - err = mapFields(recordSetResp, &model)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error reading record set", fmt.Sprintf("Processing API payload: %v", err))
    - return
  }

  - // Set refreshed state
  - diags = resp.State.Set(ctx, model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }
  - tflog.Info(ctx, "DNS record set read")
}

- // Update updates the resource and sets the updated Terraform state on success.
- func (r *recordSetResource) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) { // nolint:gocritic // function signature required by Terraform
  - // Retrieve values from plan
  - var model Model
  - diags := req.Plan.Get(ctx, &model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }

  - projectId := model.ProjectId.ValueString()
  - zoneId := model.ZoneId.ValueString()
  - recordSetId := model.RecordSetId.ValueString()
  - ctx = tflog.SetField(ctx, "project_id", projectId)
  - ctx = tflog.SetField(ctx, "zone_id", zoneId)
  - ctx = tflog.SetField(ctx, "record_set_id", recordSetId)

  - // Generate API request body from model
  - payload, err := toUpdatePayload(&model)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error updating record set", fmt.Sprintf("Creating API payload: %v", err))
    - return
  }
  - // Update recordset
  - _, err = r.client.PartialUpdateRecordSet(ctx, projectId, zoneId, recordSetId).PartialUpdateRecordSetPayload(*payload).Execute()
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error updating record set", err.Error())
    - return
  }
  - waitResp, err := wait.PartialUpdateRecordSetWaitHandler(ctx, r.client, projectId, zoneId, recordSetId).WaitWithContext(ctx)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error updating record set", fmt.Sprintf("Instance update waiting: %v", err))
    - return
  }

  - err = mapFields(waitResp, &model)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error updating record set", fmt.Sprintf("Processing API payload: %v", err))
    - return
  }
  - diags = resp.State.Set(ctx, model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }
  - tflog.Info(ctx, "DNS record set updated")
}

- // Delete deletes the resource and removes the Terraform state on success.
- func (r *recordSetResource) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) { // nolint:gocritic // function signature required by Terraform
  - // Retrieve values from plan
  - var model Model
  - diags := req.State.Get(ctx, &model)
  - resp.Diagnostics.Append(diags...)
  - if resp.Diagnostics.HasError() {
    - return
  }

  - projectId := model.ProjectId.ValueString()
  - zoneId := model.ZoneId.ValueString()
  - recordSetId := model.RecordSetId.ValueString()
  - ctx = tflog.SetField(ctx, "project_id", projectId)
  - ctx = tflog.SetField(ctx, "zone_id", zoneId)
  - ctx = tflog.SetField(ctx, "record_set_id", recordSetId)

  - // Delete existing record set
  - _, err := r.client.DeleteRecordSet(ctx, projectId, zoneId, recordSetId).Execute()
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error deleting record set", fmt.Sprintf("Calling API: %v", err))
  }
  - _, err = wait.DeleteRecordSetWaitHandler(ctx, r.client, projectId, zoneId, recordSetId).WaitWithContext(ctx)
  - if err != nil {
    - core.LogAndAddError(ctx, &resp.Diagnostics, "Error deleting record set", fmt.Sprintf("Instance deletion waiting: %v", err))
    - return
  }
  - tflog.Info(ctx, "DNS record set deleted")
}

- // ImportState imports a resource into the Terraform state on success.
- // The expected format of the resource import identifier is: project_id,zone_id,record_set_id
- func (r *recordSetResource) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
  - idParts := strings.Split(req.ID, core.Separator)
  - if len(idParts) != 3 || idParts[0] == "" || idParts[1] == "" || idParts[2] == "" {
    - core.LogAndAddError(ctx, &resp.Diagnostics,
      - "Error importing record set",
      - fmt.Sprintf("Expected import identifier with format [project_id],[zone_id],[record_set_id], got %q", req.ID),
    - )
    - return
  }

  - resp.Diagnostics.Append(resp.State.SetAttribute(ctx, path.Root("project_id"), idParts[0])...)
  - resp.Diagnostics.Append(resp.State.SetAttribute(ctx, path.Root("zone_id"), idParts[1])...)
  - resp.Diagnostics.Append(resp.State.SetAttribute(ctx, path.Root("record_set_id"), idParts[2])...)
  - tflog.Info(ctx, "DNS record set state imported")
}

- func mapFields(recordSetResp *dns.RecordSetResponse, model *Model) error {
  - if recordSetResp == nil || recordSetResp.Rrset == nil {
    - return fmt.Errorf("response input is nil")
  }
  - if model == nil {
    - return fmt.Errorf("model input is nil")
  }
  - recordSet := recordSetResp.Rrset

  - var recordSetId string
  - if model.RecordSetId.ValueString() != "" {
    - recordSetId = model.RecordSetId.ValueString()
  - } else if recordSet.Id != nil {
    - recordSetId = *recordSet.Id
  - } else {
    - return fmt.Errorf("record set id not present")
  }

  - if recordSet.Records == nil {
    - model.Records = types.ListNull(types.StringType)
  - } else {
    - records := []attr.Value{}
    - for _, record := range *recordSet.Records {
      - records = append(records, types.StringPointerValue(record.Content))
    - }
    - recordsList, diags := types.ListValue(types.StringType, records)
    - if diags.HasError() {
      - return fmt.Errorf("failed to map records: %w", core.DiagsToError(diags))
    - }
    - model.Records = recordsList
  }
  - idParts := []string{
    - model.ProjectId.ValueString(),
    - model.ZoneId.ValueString(),
    - recordSetId,
  }
  - model.Id = types.StringValue(
    - strings.Join(idParts, core.Separator),
  - )
  - model.RecordSetId = types.StringPointerValue(recordSet.Id)
  - model.Active = types.BoolPointerValue(recordSet.Active)
  - model.Comment = types.StringPointerValue(recordSet.Comment)
  - model.Error = types.StringPointerValue(recordSet.Error)
  - if model.Name.IsNull() || model.Name.IsUnknown() {
    - model.Name = types.StringPointerValue(recordSet.Name)
  - }
  - model.FQDN = types.StringPointerValue(recordSet.Name)
  - model.State = types.StringPointerValue(recordSet.State)
  - model.TTL = types.Int64PointerValue(recordSet.Ttl)
  - model.Type = types.StringPointerValue(recordSet.Type)
  - return nil
}

- func toCreatePayload(model *Model) (*dns.CreateRecordSetPayload, error) {
  - if model == nil {
    - return nil, fmt.Errorf("nil model")
  }

  - records := []dns.RecordPayload{}
  - for i, record := range model.Records.Elements() {
    - recordString, ok := record.(types.String)
    - if !ok {
      - return nil, fmt.Errorf("expected record at index %d to be of type %T, got %T", i, types.String{}, record)
    - }
    - records = append(records, dns.RecordPayload{
      - Content: conversion.StringValueToPointer(recordString),
    - })
  - }

  - return &dns.CreateRecordSetPayload{
    - Comment: conversion.StringValueToPointer(model.Comment),
    - Name:    conversion.StringValueToPointer(model.Name),
    - Records: &records,
    - Ttl:     conversion.Int64ValueToPointer(model.TTL),
    - Type:    conversion.StringValueToPointer(model.Type),
  - }, nil
}

- func toUpdatePayload(model *Model) (*dns.PartialUpdateRecordSetPayload, error) {
  - if model == nil {
    - return nil, fmt.Errorf("nil model")
  }

  - records := []dns.RecordPayload{}
  - for i, record := range model.Records.Elements() {
    - recordString, ok := record.(types.String)
    - if !ok {
      - return nil, fmt.Errorf("expected record at index %d to be of type %T, got %T", i, types.String{}, record)
    - }
    - records = append(records, dns.RecordPayload{
      - Content: conversion.StringValueToPointer(recordString),
    - })
  - }

  - return &dns.PartialUpdateRecordSetPayload{
    - Comment: conversion.StringValueToPointer(model.Comment),
    - Name:    conversion.StringValueToPointer(model.Name),
    - Records: &records,
    - Ttl:     conversion.Int64ValueToPointer(model.TTL),
  - }, nil
}

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/dns/recordset/datasource.go: DNS Record Set resource schema.

* **id** - Terraform's internal data source. ID. It is structured as "`project_id`,`zone_id`,`record_set_id`".
* **project_id** - STACKIT project ID to which the dns record set is associated.
* **zone_id** - The zone ID to which is dns record set is associated.
* **record_set_id** - The rr set id.
* **name** - Name of the record which should be a valid domain according to rfc1035 Section 2.3.4. E.g. `example.com`.
* **fqdn** - Fully qualified domain name (FQDN) of the record set.
* **records** - Records.
* **ttl** - Time to live. E.g. 3600.
* **type** - The record set type. E.g. `A` or `CNAME`.
* **active** - Specifies if the record set is active or not.
* **comment** - Comment.
* **error** - Error shows error in case create/update/delete failed.
* **state** - Record set state.

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/dns/zone/resource.go: - Resource CRUD lifecycle: create, read, update, and delete.
- Resource properties:
  - project_id
  - zone_id
  - name
  - dns_name
  - acl
  - active
  - contact_email
  - default_ttl
  - expire_time
  - is_reverse_zone
  - negative_cache
  - primaries
  - refresh_time
  - retry_time
  - serial_number
  - type
  - visibility
  - state
  - record_count

# /Users/joaopalet/Desktop/stackit/terraform-provider-stackit-copy/stackit/internal/services/dns/zone/datasource.go: Data source for retrieving DNS zone information.

"""

project_summary = get_project_summary(file_summaries)
print(project_summary)
