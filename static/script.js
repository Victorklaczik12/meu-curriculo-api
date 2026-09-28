document.addEventListener("DOMContentLoaded", async () => {
    console.log("🚀 Script JS carregado com sucesso!");

    // 1. Função para procurar as estatísticas na API e atualizar na tela
    async function carregarEstatisticas() {
        try {
            const response = await fetch("/api/analytics");
            if (response.ok) {
                const data = await response.json();
                console.log("📊 Estatísticas recebidas do servidor:", data);

                const elVisitas = document.getElementById("total-visitas");
                const elMensagens = document.getElementById("total-mensagens");

                if (elVisitas) elVisitas.innerText = data.total_visitas;
                if (elMensagens) elMensagens.innerText = data.total_mensagens;
            } else {
                console.error("❌ Erro ao buscar métricas:", response.status);
            }
        } catch (error) {
            console.error("❌ Erro na requisição de estatísticas:", error);
        }
    }

    // 2. Função para registrar a visita atual
    async function registrarVisita() {
        try {
            const response = await fetch("/api/visita", { method: "POST" });
            if (response.ok) {
                console.log("👁️ Visita registrada com sucesso!");
            }
            // Atualiza os números na tela logo após registrar
            await carregarEstatisticas();
        } catch (error) {
            console.error("❌ Erro ao registrar visita:", error);
        }
    }

    // Executa o registro de visita assim que a página abre
    await registrarVisita();

    // 3. Captura o envio do formulário de contato
    const formContacto = document.getElementById("form-contato");

    if (formContacto) {
        formContacto.addEventListener("submit", async (e) => {
            e.preventDefault();
            console.log("📩 Enviando mensagem do formulário...");

            const nome = document.getElementById("nome")?.value;
            const email = document.getElementById("email")?.value;
            const mensagem = document.getElementById("mensagem")?.value;
            const feedback = document.getElementById("status-envio") || document.getElementById("feedback-mensagem");

            try {
                const response = await fetch("/api/contacto", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ nome, email, mensagem }),
                });

                const data = await response.json();

                if (response.ok) {
                    console.log("✅ Mensagem enviada com sucesso:", data);
                    if (feedback) {
                        feedback.innerText = "Mensagem enviada com sucesso!";
                        feedback.style.color = "#16a34a";
                    }
                    formContacto.reset();
                    // Recarrega as estatísticas para subir o contador de mensagens na hora!
                    await carregarEstatisticas();
                } else {
                    console.error("❌ Erro retornado pela API:", data);
                    if (feedback) {
                        feedback.innerText = "Erro ao enviar mensagem.";
                        feedback.style.color = "#dc2626";
                    }
                }
            } catch (error) {
                console.error("❌ Erro ao enviar mensagem:", error);
            }
        });
    }
});