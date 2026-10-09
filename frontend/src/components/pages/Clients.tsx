
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

type Client = {
  id: number;
  name: string;
  phone: string;
};

const initialClients: Client[] = [
  { id: 1, name: "João Silva", phone: "53999990001" },
  { id: 2, name: "Maria Souza", phone: "53999990002" },
];

export default function Clients() {
  const [clients, setClients] = useState(initialClients);
  const [search, setSearch] = useState("");
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");

  const term = search.trim().toLocaleLowerCase("pt-BR");

  const filteredClients = clients.filter(
    (client) =>
      client.name.toLocaleLowerCase("pt-BR").includes(term) ||
      client.phone.includes(search.trim()),
  );

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const client: Client = {
      id: Math.max(0, ...clients.map((item) => item.id)) + 1,
      name: name.trim(),
      phone: phone.trim(),
    };

    setClients((current) => [...current, client]);
    setName("");
    setPhone("");
  }

  return (
    <main className="min-h-screen max-w-full bg-background p-6">
      <div className="mx-auto w-full max-w-xl space-y-6">
        <header>
          <h1 className="text-3xl font-bold">Clientes</h1>
        </header>

        <Card className="md:w-full">
          <CardHeader>
            <CardTitle>Buscar clientes</CardTitle>
          </CardHeader>
          <CardContent>
            <Input
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Pesquisar por nome ou telefone"
              aria-label="Pesquisar clientes"
            />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Novo cliente</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="client-name">Nome</Label>
                <Input
                  id="client-name"
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  required
                  maxLength={100}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="client-phone">Telefone</Label>
                <Input
                  id="client-phone"
                  type="tel"
                  value={phone}
                  onChange={(event) => setPhone(event.target.value)}
                  required
                  maxLength={20}
                />
              </div>

              <Button type="submit">Cadastrar cliente</Button>
            </form>
          </CardContent>
        </Card>

        <section className="space-y-3 mt-8">
          <h2 className="text-lg font-semibold">Resultados</h2>

          {filteredClients.length === 0 ? (
            <p className="text-sm text-muted-foreground">
              Nenhum cliente encontrado.
            </p>
          ) : (
            filteredClients.map((client) => (
              <Card key={client.id}>
                <CardContent className="flex flex-wrap items-center justify-between gap-2 p-4">
                  <span className="font-medium">{client.name}</span>
                  <span className="text-sm text-muted-foreground">
                    {client.phone}
                  </span>
                </CardContent>
              </Card>
            ))
          )}
        </section>
      </div>
    </main>
  );
}