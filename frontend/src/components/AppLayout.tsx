
import { NavLink, Outlet, useNavigate } from "react-router";
import { Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

const links = [
  { label: "Início", to: "/" },
  { label: "Clientes", to: "/clientes" },
  { label: "Peças", to: "/pecas" },
];

export default function AppLayout() {
  const navigate = useNavigate();

  function handleLogout() {
    navigate("/login");
  }

  function linkClass(isActive: boolean) {
    return `rounded-md px-3 py-2 text-sm transition-colors ${
      isActive
        ? "bg-neutral-700 text-white"
        : "text-neutral-300 hover:bg-neutral-800 hover:text-white"
    }`;
  }

  return (
    <div className="min-h-svh">
      <header className="relative z-10 flex h-16 items-center justify-between bg-neutral-900 px-4 text-white md:px-6">
        <span className="text-lg font-semibold">TorqueWeb</span>

        <nav className="absolute left-1/2 hidden -translate-x-1/2 items-center gap-2 md:flex">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.to === "/"}
              className={({ isActive }) => linkClass(isActive)}
            >
              {link.label}
            </NavLink>
          ))}
        </nav>

        <Button
          type="button"
          variant="ghost"
          onClick={handleLogout}
          className="hidden text-neutral-300 hover:bg-neutral-800 hover:text-white md:inline-flex"
        >
          Sair
        </Button> //Falta adicionar a lógica de saída

        <Sheet>
            <SheetTrigger
                render={
                    <Button
                        type="button"
                        variant="ghost"
                        size="icon"
                        aria-label="Abrir menu de navegação"
                        className="text-white hover:bg-neutral-800 hover:text-white md:hidden"
                    >
                        <Menu />
                    </Button>
  }
/>    


          <SheetContent
            side="left"
            className="border-neutral-800 bg-neutral-900 text-white"
          >
            <SheetHeader>
              <SheetTitle className="text-left text-white">
                Mecânica
              </SheetTitle>
            </SheetHeader>

            <nav className="flex flex-col gap-2 px-4">
              {links.map((link) => (
                <NavLink
                  key={link.to}
                  to={link.to}
                  end={link.to === "/"}
                  className={({ isActive }) =>
                    linkClass(isActive) + " block"
                  }
                >
                  {link.label}
                </NavLink>
              ))}

              <Button
                type="button"
                variant="ghost"
                onClick={handleLogout}
                className="mt-4 justify-start text-neutral-300 hover:bg-neutral-800 hover:text-white"
              >
                Sair
              </Button>
            </nav>
          </SheetContent>
        </Sheet>
      </header>

      <main>
        <Outlet />
      </main>
    </div>
  );
}