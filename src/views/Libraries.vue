<template>
  <div class="libraries">
    <vue-headful
      :title="$t('libraries_page_title_seo')"
      :description="$t('libraries_page_description_seo')"
    />
    <section class="section">
      <div class="container">
        <h1 class="title">{{ $t("libraries_page_header") }}</h1>
        <p class="is-size-5">{{ $t("libraries_page_description") }}</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <b-table
          :data="libraries"
          ref="table"
          detailed
          :opened-detailed="defaultOpenedDetails"
          :detail-key="name"
          :show-detail-icon="showDetailIcon"
          :hasMobileCards="true"
        >
          <template slot-scope="props">
            <b-table-column
              field="material_name"
              label="Nome do material"
              width="600"
              searchable
            >
              {{ props.row.material_name }}
            </b-table-column>

            <b-table-column field="authors" label="Autores">
              {{ props.row.authors }}
            </b-table-column>

            <b-table-column field="tags" label="Palavras chave">
              {{ props.row.tags }}
            </b-table-column>

            <b-table-column field="material_type" label="Tipo de mídia">
              {{ props.row.material_type }}
            </b-table-column>

            <b-table-column field="language" label="Idioma">
              {{ props.row.language }}
            </b-table-column>
          </template>
          <template slot="detail" slot-scope="props">
            <article class="media">
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>{{ props.row.material_name }}</strong>
                    <br />
                    <strong>Autores: </strong>{{ props.row.authors }}
                    <br />
                    <strong>Tema: </strong>{{ props.row.theme }}
                    <br />
                    <strong>Público alvo: </strong
                    >{{ props.row.target_audience }}
                    <br />
                  </p>
                  <strong>Link: </strong>
                  <div v-if="props.row.original_link !== null">
                    <a :href="props.row.original_link">{{
                      props.row.original_link
                    }}</a>
                  </div>
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
import libraries from "../assets/data/libraries_list.json";

export default {
  data() {
    return {
      libraries,
      showDetailIcon: true,
      defaultOpenedDetails: [1]
    };
  }
};
</script>
