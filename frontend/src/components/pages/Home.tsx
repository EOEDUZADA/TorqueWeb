
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table";

type WorkOrder = {
  id: number;
  client: string;
  vehicle: string;
  plate: string;
  openedAt: string;
  status: "Em andamento";
};

const initialOrders: WorkOrder[] = [
  {
    id: 1,
    client: "João Silva",
    vehicle: "Fiat Uno 2018",
    plate: "ABC1D23",
    openedAt: "08/10/2026",
    status: "Em andamento",
  },
  {
    id: 2,
    client: "Maria Souza",
    vehicle: "Volkswagen Gol 2020",
    plate: "DEF4G56",
    openedAt: "08/10/2026",
    status: "Em andamento",
  },
  {
    id: 3,
    client: "Pedro Santos",
    vehicle: "Chevrolet Onix 2022",
    plate: "GHI7J89",
    openedAt: "07/10/2026",
    status: "Em andamento",
  },
  {
    id: 4,
    client: "Ana Oliveira",
    vehicle: "Ford Ka 2019",
    plate: "JKL1M23",
    openedAt: "07/10/2026",
    status: "Em andamento",
  },
  {
    id: 5,
    client: "Carlos Pereira",
    vehicle: "Toyota Corolla 2021",
    plate: "MNO4P56",
    openedAt: "06/10/2026",
    status: "Em andamento",
  },
  {
    id: 6,
    client: "Fernanda Lima",
    vehicle: "Honda Civic 2020",
    plate: "QRS7T89",
    openedAt: "06/10/2026",
    status: "Em andamento",
  },
  {
    id: 7,
    client: "Lucas Costa",
    vehicle: "Hyundai HB20 2023",
    plate: "UVW1X23",
    openedAt: "05/10/2026",
    status: "Em andamento",
  },
  {
    id: 8,
    client: "Beatriz Rocha",
    vehicle: "Renault Sandero 2019",
    plate: "YZA4B56",
    openedAt: "05/10/2026",
    status: "Em andamento",
  },
];

const PAGE_SIZE = 5;

export default function Home() {
  const [search, setSearch] = useState("");
  const [currentPage, setCurrentPage] = useState(1);

  const term = search.trim().toLocaleLowerCase("pt-BR");

  const filteredOrders = initialOrders.filter((order) =>
    [
      String(order.id),
      order.client,
      order.vehicle,
      order.plate,
    ].some((value) =>
      value.toLocaleLowerCase("pt-BR").includes(term),
    ),
  );

  const totalPages = Math.max(
    1,
    Math.ceil(filteredOrders.length / PAGE_SIZE),
  );

  const page = Math.min(currentPage, totalPages);
  const startIndex = (page - 1) * PAGE_SIZE;

  const visibleOrders = filteredOrders.slice(
    startIndex,
    startIndex + PAGE_SIZE,
  );

  function handleSearch(value: string) {
    setSearch(value);
    setCurrentPage(1);
  }

  return (
    <main className="flex min-h-screen w-full items-center bg-background p-4 md:p-8">
      <div className="mx-auto w-full max-w-7xl space-y-6">
        <header className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div className="space-y-1">
            <h1 className="text-3xl font-bold tracking-tight">
              Ordens de serviço
            </h1>
          </div>

          <Button>
            Adicionar
          </Button>
        </header>

        <section className="space-y-4">
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <Input
              value={search}
              onChange={(event) => handleSearch(event.target.value)}
              placeholder="Buscar por OS, cliente, veículo ou placa..."
              aria-label="Buscar ordens de serviço"
              className="w-full sm:max-w-md"
            />

            <p className="text-sm text-muted-foreground">
              {filteredOrders.length}{" "}
              {filteredOrders.length === 1
                ? "ordem encontrada"
                : "ordens encontradas"}
            </p>
          </div>

          
<Table className="min-w-[750px]">
  <TableHeader>
    <TableRow className="bg-muted/50 hover:bg-muted/50">
      <TableHead>OS</TableHead>
      <TableHead>Cliente</TableHead>
      <TableHead>Veículo</TableHead>
      <TableHead>Placa</TableHead>
      <TableHead>Abertura</TableHead>
      <TableHead>Status</TableHead>
    </TableRow>
  </TableHeader>

  <TableBody>
    {visibleOrders.map((order) => (
      <TableRow key={order.id}>
        <TableCell className="font-medium">
          #{String(order.id).padStart(3, "0")}
        </TableCell>
        <TableCell>{order.client}</TableCell>
        <TableCell>{order.vehicle}</TableCell>
        <TableCell className="font-mono">{order.plate}</TableCell>
        <TableCell>{order.openedAt}</TableCell>
        <TableCell>
          <span className="inline-flex whitespace-nowrap rounded-full bg-green-100 px-2.5 py-1 text-xs font-medium text-green-800 dark:bg-green-950 dark:text-green-300">
            {order.status}
          </span>
        </TableCell>
      </TableRow>
    ))}

    {visibleOrders.length === 0 && (
      <TableRow>
        <TableCell
          colSpan={6}
          className="h-24 text-center text-muted-foreground"
        >
          Nenhuma ordem de serviço encontrada.
        </TableCell>
      </TableRow>
    )}
  </TableBody>
</Table>

          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <p className="text-sm text-muted-foreground">
              {filteredOrders.length > 0
                ? `Exibindo ${startIndex + 1}–${Math.min(
                    startIndex + PAGE_SIZE,
                    filteredOrders.length,
                  )} de ${filteredOrders.length} ordens`
                : "Nenhuma ordem para exibir"}
            </p>

            <div className="flex items-center gap-2">
              <Button
                variant="outline"
                size="sm"
                disabled={page <= 1}
                onClick={() => setCurrentPage((current) => current - 1)}
              >
                Anterior
              </Button>

              <span className="min-w-20 text-center text-sm">
                Página {page} de {totalPages}
              </span>

              <Button
                variant="outline"
                size="sm"
                disabled={page >= totalPages}
                onClick={() => setCurrentPage((current) => current + 1)}
              >
                Próxima
              </Button>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}