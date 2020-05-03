<template>
  <div class="services">
    <vue-headful
      :title="$t('services_page_title_seo')"
      :description="$t('services_page_description_seo')"
    />
    <section class="section">
      <div class="container">
        <h1 class="title">{{ $t("services_page_header") }}</h1>
        <p class="is-size-5">{{ $t("services_page_description") }}</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <b-table
          :data="services"
          ref="table"
          detailed
          :opened-detailed="defaultOpenedDetails"
          :detail-key="name"
          :show-detail-icon="showDetailIcon"
          :hasMobileCards="true"
        >
          <template slot-scope="props">
            <b-table-column
              field="name"
              label="Nome do Serviço"
              width="300"
              searchable
            >
              {{ props.row.name }}
            </b-table-column>

            <b-table-column field="covid_related" label="COVID-19">
              {{ props.row.covid_related }}
            </b-table-column>

            <b-table-column field="service_remote" label="Remoto">
              {{ props.row.service_remote }}
            </b-table-column>

            <b-table-column field="service_type" label="Tipo de serviço">
              {{ props.row.service_typ }}
            </b-table-column>

            <b-table-column field="service_language" label="Idioma">
              {{ props.row.service_language }}
            </b-table-column>
          </template>
          <template slot="detail" slot-scope="props">
            <article class="media">
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>{{ props.row.name }}</strong>
                    <br />
                    <strong>Descrição: </strong
                    >{{ props.row.service_description }}
                    <br />
                    <strong>Observações: </strong>{{ props.row.observations }}
                    <br />
                    <strong>Link: </strong>
                    <a :href="props.row.service_url">Clique aqui</a>
                    <br />
                    <strong>Telefone: </strong> {{ props.row.telephone }}
                    <br />
                    <strong>E-mail: </strong> {{ props.row.email }}
                    <br />
                  </p>
                </div>
              </div>
            </article>
          </template>
        </b-table>
      </div>
    </section>
  </div>
</template>
<script>
import services from "../assets/data/services_list.json";

export default {
  data() {
    return {
      services,
      showDetailIcon: true,
      defaultOpenedDetails: [1]
    };
  }
};
</script>
