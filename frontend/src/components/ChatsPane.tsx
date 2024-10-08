import CloseRoundedIcon from "@mui/icons-material/CloseRounded";
import EditNoteRoundedIcon from "@mui/icons-material/EditNoteRounded";
import SearchRoundedIcon from "@mui/icons-material/SearchRounded";
import { Box, Chip, IconButton, Input, ModalDialogProps } from "@mui/joy";
import List from "@mui/joy/List";
import Sheet from "@mui/joy/Sheet";
import Stack from "@mui/joy/Stack";
import Typography from "@mui/joy/Typography";
import React from "react";
import { ChatProps } from "../types/types";
import { toggleMessagesPane } from "../utils/ChatRoomUtils";
import ChatListItem from "./ChatListItem";
import ColorSchemeToggle from "./ColorSchemeToggle";
import DialogVerticalScroll from "./DialogVerticalScroll";

type ChatsPaneProps = {
  chats: ChatProps[];
  setSelectedChat: (chat: ChatProps) => void;
  selectedChatId: string;
};

export default function ChatsPane(props: ChatsPaneProps) {
  const { chats, setSelectedChat, selectedChatId } = props;
  const [layout, setLayout] = React.useState<
    ModalDialogProps["layout"] | undefined
  >(undefined);

  return (
    <Sheet
      sx={{
        borderRight: "1px solid",
        borderColor: "divider",
        height: { sm: "calc(100dvh - var(--Header-height))", md: "100dvh" },
        overflowY: "auto",
      }}
    >
      <Stack
        direction="row"
        spacing={1}
        sx={{
          alignItems: "center",
          justifyContent: "space-between",
          p: 2,
          pb: 1.5,
        }}
      >
        <Typography
          component="h1"
          endDecorator={
            <Chip
              variant="soft"
              color="primary"
              size="md"
              slotProps={{ root: { component: "span" } }}
            >
              4
            </Chip>
          }
          sx={{
            fontSize: { xs: "md", md: "lg" },
            fontWeight: "lg",
            mr: "auto",
          }}
        >
          Messages
        </Typography>
        <Stack
          direction="row"
          spacing={1}
          sx={{
            alignItems: "center",
            justifyContent: "space-between",
            p: 1,
            pb: 1.5,
          }}
        >
          <IconButton
            variant="plain"
            aria-label="edit"
            color="neutral"
            size="sm"
            onClick={() => setLayout("center")}
            // sx={{ display: { xs: "none", sm: "unset" } }}
          >
            <EditNoteRoundedIcon />
          </IconButton>
          <DialogVerticalScroll layout={layout} setLayout={setLayout} />
          <IconButton
            variant="plain"
            aria-label="edit"
            color="neutral"
            size="sm"
          >
            <ColorSchemeToggle />
          </IconButton>
          <IconButton
            variant="plain"
            aria-label="edit"
            color="neutral"
            size="sm"
            onClick={() => {
              toggleMessagesPane();
            }}
            sx={{ display: { sm: "none" } }}
          >
            <CloseRoundedIcon />
          </IconButton>
        </Stack>
      </Stack>
      <Box sx={{ px: 2, pb: 1.5 }}>
        <Input
          size="sm"
          startDecorator={<SearchRoundedIcon />}
          placeholder="Search"
          aria-label="Search"
        />
      </Box>
      <List
        sx={{
          py: 0,
          "--ListItem-paddingY": "0.75rem",
          "--ListItem-paddingX": "1rem",
        }}
      >
        {chats.map((chat) => (
          <ChatListItem
            key={chat.id}
            {...chat}
            setSelectedChat={setSelectedChat}
            selectedChatId={selectedChatId}
          />
        ))}
      </List>
    </Sheet>
  );
}
